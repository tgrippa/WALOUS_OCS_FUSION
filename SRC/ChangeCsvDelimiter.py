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

import os, csv, shutil

def ChangeCsvDelimiter(in_file, sep, new_sep, out_file=''):
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

#testD
#test2
#test3
