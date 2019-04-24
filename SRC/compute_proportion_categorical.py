#!/usr/bin/env python

from __main__ import *

import os
import csv
import grass.script as gscript
import tempfile


def proportion_class_rstats(rasterLayer, zone_map, cl_list):
    '''
    Function computing by-segment class proportion from a categorical raster. 
    'rasterLayer' wait for the name of the categorical raster.
    'zone_map' wait for the name of the zones/segmentation raster.
    'cl_list' wait for a list with the class values expected in the categorical raster.
    The computational region should be defined properly before running this function.
    '''
    import csv
    tmpfile = gscript.tempfile()
    gscript.run_command('r.stats', overwrite=True, flags='cn', input='%s,%s'%(zone_map,rasterLayer), output=tmpfile, separator=',')
 
    # Get list of categories to output
    class_dict = {str(a):"" for a in cl_list}  #To be sure it's string format
    
    # Open file and create a csv reader
    csvfile = open(tmpfile, 'r')
    reader = csv.reader(csvfile, delimiter=',')

    # Total pixels per category per zone
    totals_dict = {}
    for row in reader:
        if row[0] not in totals_dict: # Will pass only if the current SegID don't exist in dictionary
            totals_dict[row[0]] = {} # Declare a new embedded dictionnary for the current SegID
        totals_dict[row[0]][row[1]] = int(row[2])

    # Proportion of each category per zone
    percents_dict = {}
    percents_dict
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
    # Create output file and create a csv writer
    outfile = os.path.join(gscript.tempdir(),'%s_prop_%s.csv'%(zone_map,rasterLayer))
    csvfile = open(outfile, 'w')
    writer = csv.writer(csvfile, delimiter=',')
    header = ['cat',]
    [header.append('prop_%s'%cl) for cl in class_list]
    writer.writerow(header)
    for k in percents_dict:
        newrow = [k,]
        for cl in class_list:
            newrow.append(percents_dict[k]['%s'%cl])
        writer.writerow(newrow)
    csvfile.close()
    return outfile