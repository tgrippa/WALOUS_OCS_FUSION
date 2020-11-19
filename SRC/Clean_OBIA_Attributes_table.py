# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:50:40 2019

@author: tais
"""

"""
WALOUS_OCS_FUSION - Copyright (C) <2020> <Service Public de Wallonie (SWP), Belgique,
					          		Institut Scientifique de Service Public (ISSeP), Belgique,
									Université catholique de Louvain (UCLouvain), Belgique,
									Université Libre de Bruxelles (ULB), Belgique>
						 							
	
List of the contributors to the development of WALOUS_OCS_FUSION: see LICENSE file.
Description and complete License: see LICENSE file.
	
This program (WALOUS_OCS_FUSION) is free software: 
you can redistribute it and/or modify it under the terms of the 
GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) 
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (see COPYING file).  If not, 
see <http://www.gnu.org/licenses/>.
"""

import glob
import gzip
import pandas as pd


def decompress_gzip(in_path, out_path):
    inF = gzip.GzipFile(in_path, 'r')
    s = inF.read()
    inF.close()

    outF = open(out_path, 'w')
    outF.write(s)
    outF.close()

def compress_gzip(in_path, out_path):
    inF = open(in_path, 'r')
    s = inF.read()
    inF.close()

    outF = gzip.GzipFile(out_path, 'w')
    outF.write(s)
    outF.close()

def CutCsv(input_csv, indexcol=[], nb_col_from_end=[]):
    import subprocess, sys
    # Check if at least one option is asked
    if not indexcol and not nb_col_from_end:
        return "ERROR: At least parameter 'indexcol' or 'nb_col_from_end' should be provided"
        sys.exit()
    # Create a new .csv with only the first and the X lasts columns (X = nb_col_from_end. By default, first and last only)
    path, ext = os.path.splitext(input_csv)
    cut_csv = "%s_cut%s"%(path,ext)
    f = open(cut_csv, "w")
    if nb_col_from_end:
        # Get number of colums in the .csv
        p1 = subprocess.Popen(("head -1 %s"%input_csv).split(), stdout=subprocess.PIPE)
        p2 = subprocess.Popen(("tr ',' '\\n'").split(), stdin=p1.stdout, stdout=subprocess.PIPE)
        p3 = subprocess.Popen(("wc -l").split(), stdin=p2.stdout, stdout=subprocess.PIPE)
        nb_columns = int(p3.communicate()[0])
        index_start = nb_columns-nb_col_from_end
    if indexcol and not nb_col_from_end:
        subprocess.Popen(("cut -d, -f1,%s %s"%(','.join(indexcol),input_csv)).split(), stdout=f)
    if nb_col_from_end and not indexcol:
        subprocess.Popen(("cut -d, -f1,%s-%s %s"%(index_start,nb_columns,input_csv)).split(), stdout=f)
    if nb_col_from_end and indexcol:
        subprocess.Popen(("cut -d, -f1,%s,%s-%s %s"%(','.join(indexcol),index_start,nb_columns,input_csv)).split(), stdout=f)
    f.close()
    return cut_csv

def ChangeCsvDelimiter(in_file, sep, new_sep, out_file=''):
    import os, csv, shutil
    # Parameters for tempfile (path and sep)
    path, ext = os.path.splitext(in_file)
    tmp_file = "%s_tmp%s"%(path,ext)

    with open(in_file,'r') as f_in, open(tmp_file,'w') as f_out:
        csvreader = csv.reader(f_in, delimiter=sep)
        csvwriter = csv.writer(f_out, delimiter=new_sep)
        for in_row in csvreader:
            csvwriter.writerow(in_row)
        f_in.close()
        f_out.close()
    # Overwrite existing input file it 'out_file' not specified
    if out_file == '':
        os.remove(in_file)
        shutil.copy2(tmp_file,in_file)
        os.remove(tmp_file)
    else:
        shutil.copy2(tmp_file,out_file)
        os.remove(tmp_file)

def CleanCSV_OBIA_ATTRIBUTES(compress_path):
    zone = compress_path.split("/")[-3]
    decompress_path = compress_path[:-3]
    decompress_gzip(compress_path, decompress_path)
    if zone == "HERVE":
        ChangeCsvDelimiter(decompress_path, '|',',') # ONLY needed for HERVE
        cut_path = CutCsv(decompress_path, nb_col_from_end=9)
    if zone in ("CHARLEROI","ARLON"):
        cut_path = CutCsv(decompress_path, nb_col_from_end=10)
    if zone == "MARCHE":
        cut_path = CutCsv(decompress_path, nb_col_from_end=11)
    time.sleep(10)
    df = pd.read_csv(cut_path, sep=',')
    os.remove(cut_path)
    os.remove(decompress_path)
    if zone in ("HERVE", "CHARLEROI", "MARCHE", "ARLON"):
        df.drop(columns=["prob_max",], inplace=True)
    if zone in ("CHARLEROI","MARCHE"):
        df.drop(columns=["color_class",], inplace=True)
    if zone in ("MARCHE","ARLON"):
        df.drop(columns=["part",], inplace=True)
        df.rename(index=str, columns={"class": "rf_class"}, inplace=True)
    df.to_csv(decompress_path, index=False)
    compress_gzip(decompress_path, compress_path)
    os.remove(decompress_path)


#list_csv = glob.glob("/media/tais/data/WALOUS/Data/obia_2016/HERVE/ATTRIBUTS/*.csv.gz")
#list_csv = glob.glob("/media/tais/data/WALOUS/Data/obia_2016/CHARLEROI/ATTRIBUTS/*.csv.gz")
#list_csv = glob.glob("/media/tais/data/WALOUS/Data/obia_2016/MARCHE/ATTRIBUTS/*.csv.gz")
list_csv = glob.glob("/media/tais/data/WALOUS/Data/obia_2016/ARLON/ATTRIBUTS/*.csv.gz")

#list_csv = ["/media/tais/data/WALOUS/Data/obia_2016/HERVE/ATTRIBUTS/segs_tile68_stats.csv.gz",]

# Loop
for compress_path in list_csv[:1]:
    CleanCSV_OBIA_ATTRIBUTES(compress_path)

# Parallel
import multiprocessing
from multiprocessing import Pool
from functools import partial

p = Pool(15)
output = p.map(CleanCSV_OBIA_ATTRIBUTES, list_csv)  # Launch the processes for as many items in the list (if function with a return, the returned results are ordered thanks to 'map' function)
p.close()
p.join()