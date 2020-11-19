#!/usr/bin/env python

"""
Functions for compression and decompressing gzip files
http://xahlee.info/python/gzip.html

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

import gzip

def decompress_gzip(in_path, out_path):
	inF = gzip.GzipFile(in_path, 'rb')
	s = inF.read()
	inF.close()

	outF = file(out_path, 'wb')
	outF.write(s)
	outF.close()
	
def compress_gzip(in_path, out_path):
	inF = file(in_path, 'rb')
	s = inF.read()
	inF.close()

	outF = gzip.GzipFile(out_path, 'wb')
	outF.write(s)
	outF.close()