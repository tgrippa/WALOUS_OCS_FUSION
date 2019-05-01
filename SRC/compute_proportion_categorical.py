#!/usr/bin/env python

from __main__ import *

import os
import csv
import grass.script as gscript
import csv
import operator

def CategoStats(rasterLayer, zone_map, cl_list=[], colpref="", prop=True, mode=True, countnullformode=True):
    '''
    Function computing by-segment class proportion from a categorical raster.
    'rasterLayer' wait for the name of the categorical raster.
    'zone_map' wait for the name of the zones/segmentation raster.
    'cl_list' wait for a list with the class values expected in the categorical raster. If this list is provided, the class not existing in the output of r.stats will be filled with ZERO
    The computational region should be defined properly before running this function.
    '''
    # Check parameters
    if not prop and not mode:
        return "ERROR : At least 'prop' or 'mode' should be TRUE"

    # r.stats
    tmpfile = gscript.tempfile()
    if countnullformode:
        gscript.run_command('r.stats', overwrite=True, flags='c', input='%s,%s'%(zone_map,rasterLayer), output=tmpfile, separator=',') #R.STATS with pixel count including 'null'
    else:
        gscript.run_command('r.stats', overwrite=True, flags='cn', input='%s,%s'%(zone_map,rasterLayer), output=tmpfile, separator=',') #R.STATS with pixel count including 'null'

    # Open csv file and create a csv reader
    csvfile = open(tmpfile, 'r')
    reader = csv.reader(csvfile, delimiter=',')

    # Total pixels per category per zone
    totals_dict = {}
    for row in reader:
        if row[0] not in totals_dict: # Will pass the condition only if the current zone ID does not exists in the dictionary
            totals_dict[row[0]] = {} # Declare a new embedded dictionnary for the current zone ID
        totals_dict[row[0]][row[1]] = int(row[2])
    # Delete key '*' in 'totals_dict' that could append if there are null values on the zone raster
    if "*" in totals_dict:
        del totals_dict["*"]
    
    ### MODAL VALUE
    # modal class of each zone
    if mode:
        modalclass_dict = {}
        for k in totals_dict:
            mode = max(totals_dict[k].iteritems(), key=operator.itemgetter(1))[0] # The trick was found here : https://stackoverflow.com/a/268285/8013239
            if mode =="*":   # If the mode is NULL values
                modalclass_dict[k] = ""
            else:
                modalclass_dict[k] = mode

    ### PROPORTIONS
    if prop:
        # Get list of categories to output
        if cl_list:   #If list of classes provided by user
            class_dict = {str(a):"" for a in cl_list}  #To be sure it's string format
        else:
            class_dict = {}

        # Remove null values (mandatory for the computation of proportions)
        for k in totals_dict:
            if '*' in totals_dict[k].keys():
                del totals_dict[k]["*"]

        # Proportion of each category per zone (excluding nulls)
        percents_dict = {}
        for k in totals_dict:
            percents_dict[k] = {}
            for k2 in totals_dict[k]:
                percents_dict[k][k2] = float(totals_dict[k][k2]) / sum(totals_dict[k].values())
                class_dict[k2] = ""  #Add this class to the dictionnary of classes

        # Fill class not met with zero
        for k in percents_dict:
            for cl in class_dict:
                if cl not in percents_dict[k]:
                    percents_dict[k][cl] = 0

        # Get list of class sorted by value (arithmetic)
        class_list = [int(k) for k in class_dict.keys()]
        class_list.sort()

    ### OUTPUT

    # Create output file and create a csv writer
    outfile = os.path.join(gscript.tempdir(),'categostats_%s_%s.csv'%(zone_map,rasterLayer))
    csvfile = open(outfile, 'w')
    writer = csv.writer(csvfile, delimiter=',')
    # Write header
    header = ['cat',]
    if mode:
        if colpref == "":
            header.append('mode')
        else:
            header.append('%s_mode'%colpref)
    if prop:
        if colpref == "":
            [header.append('prop_%s'%cl) for cl in class_list]
        else:
            [header.append('%s_prop_%s'%(colpref,cl)) for cl in class_list]
    writer.writerow(header)

    # Write content
    for k in totals_dict:
        newrow = [k,]  #Zone ID
        if mode:
                newrow.append(modalclass_dict[k])
        if prop:
            for cl in class_list:
                newrow.append(percents_dict[k]['%s'%cl])
        writer.writerow(newrow)
    csvfile.close()
    return outfile


