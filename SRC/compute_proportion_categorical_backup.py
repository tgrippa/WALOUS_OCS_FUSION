#!/usr/bin/env python

from __main__ import *

import os
import csv
import grass.script as gscript
import tempfile

def proportion_class(rasterLayer, zone_map, cl):
    '''
    Function extracting a binary map for class 'cl' in raster 'rasterLayer', then computing the proportion of this class.
    The computational region should be defined properly before running this function.
    '''
    def random_layer_name(prefix='tmp'):
        ### Function that return a name for a temporary layer in GRASS GIS ###
        tmp = gscript.tempfile()
        return prefix + '_' +gscript.basename(tmp).replace('.','_')

    def compute_proportion_csv(infile):
        '''
        Function used in 'proportion_class' function. It take as input the csv from i.segment.stats with the area (in number of pixels)
        the sum of pixels of the binary raster and create a new csv with the proportion
        '''
        # Set the path to the outputfile
        head, tail = os.path.split(infile)
        root, ext = os.path.splitext(tail)
        outfile=os.path.join(head,root+"_prop"+ext)
        # Create new csv reader and writer objects
        reader=csv.reader(open(infile,'r'), delimiter=",")
        writer=csv.writer(open(outfile,'w'), delimiter=",")
        # Initialize empty lists
        crash_report=[]
        content=[]
        # Save the first line as header and create the new header
        header=reader.next()
        new_header=[]
        new_header.append(header[0])
        index=header[2].find("_sum")
        new_header.append(header[2][:index]+'_proportion')
        content.append(new_header)  #Create new header with first original column and current class related name for proportion
        # Loop through the rest of the rows (header is passed)
        for row in reader:
            pix_nb=float(row[1]) #Area of the unit (in number of pixels)
            class_nb=float(row[2]) #Number of pixels of current class (binary raster)
            try:
                prop=100*class_nb/pix_nb
                content.append([row[0],"{0:.5f}".format(prop)])
            except ZeroDivisionError:  #If computation of proportion failed because of 'ZeroDivisionError'
                crash_report.append(row[0])
                content.append([row[0],"{0:.5f}".format(0.0)])  # If ZeroDivisionError, set the proportion to zero to avoid errors in next steps
                continue
        writer.writerows(content)
        os.remove(infile)
        # Print notification of ZeroDivisionError if it happened
        if len(crash_report)>0:
            print "An 'ZeroDivisionError' has been registered for the following <%s>"%header[0]+"\n".join(crash_report)
        # Return the path to the temporary csv file
        return outfile

    binary_raster = "%s_cl_%s"%(rasterLayer,cl)  # Set the name of the binary raster
    gscript.run_command('r.mapcalc', expression='%s=if(%s==%s,1,0)'%(binary_raster,rasterLayer,cl),
                        overwrite=True,quiet=True) # Mapcalc to create binary raster for the expected class 'cl'
    ### Create a temporary copy of the current binary raster with all pixels values equal to 1 (to be used for computing proportion of current binary class)
    tmplayer = random_layer_name(prefix='tmp_%s'%binary_raster)
    gscript.run_command('r.mapcalc', expression='%s=if(%s==1,1,1)'%(tmplayer,rasterLayer),
                        overwrite=True,quiet=True)
    # Fill potential remaining null values with 0 value (when using r.mapcalc, null values existing in the 'rasterLayer' will remain null in the binary)
    gscript.run_command('r.null', quiet=True, map=binary_raster, null='0')
    gscript.run_command('r.null', quiet=True, map=tmplayer, null='0')
        
    ### Compute proportion of pixels of the current class - Grids
    stat_csv=os.path.join(tempfile.gettempdir(),"%s_cl_%s.csv"%(rasterLayer,cl))
    gscript.run_command('i.segment.stats', flags='cs', map=zone_map, rasters='%s,%s'%(tmplayer,binary_raster), raster_statistics='sum', csvfile=stat_csv, separator='comma', quiet=True, overwrite=True)
    output_csv=compute_proportion_csv(stat_csv) #Create a new csv containing the proportion

    ### Remove temporary layer
    gscript.run_command('g.remove', quiet=True, flags='f',type='raster',name=tmplayer)
    # Return lists
    return (binary_raster,output_csv)

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