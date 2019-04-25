# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:23:46 2019

@author: tais
"""

import csv

def CsvChangeEmptyByO(inputcsv, sep=','):
    fin=open(inputcsv,"r")
    readercsv=csv.reader(fin, delimiter=sep)

    out = []
    out.append(readercsv.next())
    for row in readercsv:
        newrow = []
        for value in row:
            if not value:  # If the value is empty
                newrow.append("0")
            else:
                newrow.append(value)
        out.append(newrow)
    fin.close()

    fout=open(inputcsv,"w")
    writercsv=csv.writer(fout, delimiter=sep)
    writercsv.writerows(out)
    fout.close()



#inputcsv = "/media/tais/data/WALOUS/Results/Classification_features/features_tile_68.csv"
#CsvChangeEmptyByO(inputcsv, sep=',')