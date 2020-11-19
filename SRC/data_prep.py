#!/usr/bin/env python

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

import os
import grass.script as gscript


def data_prep(categorical_raster):
    '''
    Function that extracts resolution and sorted list of classes of 
    a categorical raster (like land cover or land use information).
    '''
    info = gscript.raster_info(categorical_raster)
    nsres=info.nsres
    ewres=info.ewres
    L = []
    L=[cl.split("	")[0] for cl in gscript.parse_command('r.category',map=categorical_raster)]
    for i,x in enumerate(L):  #Make sure the format is UTF8 and not Unicode
        L[i]=x.encode('UTF8')
    L.sort(key=float) #Sort the raster categories in ascending.
    return nsres, ewres, L