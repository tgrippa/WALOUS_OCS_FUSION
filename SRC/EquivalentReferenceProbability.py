#!/usr/bin/env python

"""
This function is used to compute ERP (Equivalent Reference Probability) from a csv file with membership probabilities to different classes

"""

import csv, os, sys, math, tempfile

def ComputeERPfromCsv(in_path, delimiter=',', erp_name="ERP", start_index=1, stop_index=False):   # "start_index" should contain the index where probabilities starts, "stop_index" where it stops.
    # Open files and create reader
    infile = open(in_path, 'r')
    reader = csv.reader(infile, delimiter=delimiter)

    # Csv header
    out_header = reader.next() #Get the header (first line) of input csv
    out_header.append(erp_name)

    # Create list containing output content
    out_content = []
    out_content.append(out_header) #Add the output header

    # Compute ERP values from probabilities and store new lines in a list
    for row in reader:
        out_line = row  # Copy the input file line
        if stop_index:
            frow = [float(x) for x in row[start_index:stop_index+1]] #Make sure all columns are float except for Xth first column (parameter "start_index")
        else:
            frow = [float(x) for x in row[start_index:]] #Make sure all columns are float except for Xth first column (parameter "start_index")
        probs = [x/sum(frow) for x in frow] #Make sure that the sum of probabilities equal to 1
        maxpistar = max(probs) #Take the maximum probability
        temp = [x for x in probs if x!=maxpistar] #Take probability of all but the class with the max probability
        tempEnt = [y*math.log(y) for y in temp if y>0] # If the probability is equal to zero, then the entropy will be zero
        if (1-maxpistar) > 0:
            EDI = math.log(maxpistar)-sum(tempEnt)/(1-maxpistar)
            out_line.append(math.exp(EDI)/(math.exp(EDI)+len(probs)-1))
        else:
            out_line.append(1)
        out_content.append(out_line)

    # Create output file
    out_path = "%s_ERP.csv"%os.path.splitext(in_path)[0]
    outfile = open(out_path, 'w')
    writer = csv.writer(outfile, delimiter=delimiter)
    writer.writerows(out_content)

    # Return
    return out_path

#in_path = "/media/tais/data/WALOUS/Processing/GRASSDATA/WALOUS_31370/68/.tmp/tais-HP-Z620-Workstation/17378.1/segmentation_prop_ortho_lc.csv"
#ComputeERPfromCsv(in_path, erp_name="orth_lc_ERP")

#in_path = "/media/tais/data/WALOUS/Data/obia_2016/HERVE/ATTRIBUTS/segs_tile68_stats.csv"
#ComputeERPfromCsv(in_path, erp_name="OBIA_ERP", start_index=2)
