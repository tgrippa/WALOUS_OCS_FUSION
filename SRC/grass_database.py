#!/usr/bin/env python

"""
Functions for automatic check and creation of GRASS GIS database folders
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

import os
import grass.script as gscript
import grass.script.setup as gsetup
import shutil ## Import library for file copying 


def check_gisdb(gisdb_path):
	## Automatic creation of GRASSDATA folder
	if os.path.exists(gisdb_path):
		return "GRASSDATA folder already exist" 
	else: 
		os.makedirs(gisdb_path) 
		return "GRASSDATA folder created in '%s'"%gisdb_path
		
def check_location(gisdb_path,location_name,epsg):
	## Automatic creation of GRASS location is doesn't exist
	if os.path.exists(os.path.join(gisdb_path,location_name)):
		return "Location '%s' already exist"%location_name
	else : 
		gscript.core.create_location(gisdb_path, location_name, epsg=epsg, overwrite=False)
		return "Location '%s' created"%location_name
	
def check_mapset(gisdb_path,location_name,mapset_name):
	### Automatic creation of GRASS GIS mapsets
	if os.path.exists(os.path.join(gisdb_path,location_name,"PERMANENT")):  # Check if PERMANENT mapset exists because it is needed
		if not os.path.exists(os.path.join(gisdb_path,location_name,"PERMANENT",'WIND')): # Check if PERMANENT mapset exists because it is needed
			return "WARNING: 'PERMANENT' mapset already exist, but a 'WIND' file is missing. Please solve this issue."
		else: 
			if not os.path.exists(os.path.join(gisdb_path,location_name,mapset_name)):
				os.makedirs(os.path.join(gisdb_path,location_name,mapset_name))
				shutil.copy(os.path.join(gisdb_path,location_name,'PERMANENT','WIND'),os.path.join(gisdb_path,location_name,mapset_name,'WIND'))
				return "'%s' mapset created in location '%s'"%(mapset_name,location_name)
			else:
				return "'%s' mapset already exists in location '%s'"%(mapset_name,location_name)
	else:
		return "WARNING: 'PERMANENT' mapset do not exist. Please solve this issue."

def working_mapset(gisdb_path,location_name,mapset_name):
	## Launch GRASS GIS working session in the mapset
	if os.path.exists(os.path.join(gisdb_path,location_name,mapset_name)):
		gsetup.init(os.environ['GISBASE'], gisdb_path,location_name,mapset_name)
		return "You are now working in mapset '%s/%s'"%(location_name,mapset_name)
	else: 
		return "'%s' mapset doesn't exists in '%s'"%(mapset_name,gisdb_path)