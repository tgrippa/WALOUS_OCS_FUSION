# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:23:46 2019

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