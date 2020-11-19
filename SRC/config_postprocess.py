#!/usr/bin/env python

"""
This script is used to store all configuration parameter to run the main code (jupyter notebook)

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

# Initialize dictionnaries
config_parameters = {}
data = {}


## Please update the following paths according to your own configuration
config_parameters['GRASSBIN'] = '/usr/bin/grass78'
config_parameters['GISBASE'] = '/usr/lib64/grass78'
#config_parameters['PYTHONLIB'] = '/usr/lib/python2.7'
config_parameters['PYTHONLIB'] = '/usr/bin/python2.7' 
config_parameters['locationepsg'] = '31370' #  EPSG code for Belgian Lambert 1972
config_parameters['njobs'] = 6

## The following parameters should not be changed normally
config_parameters['gisdb'] = '../GRASSDATA' # path to GRASSDATA folder
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['outputfolder'] = '../fusion/RF_fusion/Postprocess6'
config_parameters['location'] = "WALOUS_31370"

## Other folder for automatic output
config_parameters['outputfolder_Logfile'] = os.path.join(config_parameters['outputfolder'],"Log_file")
config_parameters['outputfolder_Raster'] = os.path.join(config_parameters['outputfolder'],"Raster")
config_parameters['outputfolder_Vecteur'] = os.path.join(config_parameters['outputfolder'],"Vecteur")

## Other path
config_parameters['list_tiles'] = os.path.join(config_parameters['outputfolder'],"list_tiles")

## The following path linking to datasets should be changed according to your own folder organization
data['tiles'] = ('tiles','../fusion/tuilesRW/FUSION_TUILAGE_ULB_31370.shp') # Processing tiles
data['fusion_folder'] = ('fusion_lc','../fusion/RF_fusion/Postprocess6/RF_tiles')
data['fusion_folder'] = ('fusion_lc','../fusion/RF_fusion/Results_RW/fusion_bytile_LB72')
data['binary_agri'] = ('SIGEC','../fusion/RF_fusion/data/RW/sigec/SIGEC_WALLONIE_2018_31370_uint8.tif') # 10 m res.
data['binary_forest'] = ('forest','../fusion/RF_fusion/data/RW/forest/masque_forest_3classes.tif')# 2 m res.
data['binary_hydro'] = ('hydro','../../../Data/squelette_vectoriel/Hydro_mask_31370.tif') # 2 m res.
data['binary_roadnet'] = ('roadnet','../../../Data/squelette_vectoriel/Roadnet_mask_31370.tif') # 2 m res.
data['binary_built'] = ('built','../../../Data/squelette_vectoriel/Buildings_mask_31370.tif') # 1 m res.
data['binary_rail'] = ('rail','../../../Data/squelette_vectoriel/rail.tif') # 1 m res.
#data['communes'] = ('communes','../../../Data/Communes_BEL/com_bel.shp') # EPSG:31370
#data['CaPa'] = ('CaPa','../../../../Landuse/Data/Plan_cadastral/01000_Belgium_PP-FiscSit_Lb2008_01012019/Bpn_CaPa.shp') # EPSG:3812

## Color rule file
data['color_file'] = "../fusion/RF_fusion/fusion_colors.txt"
#"/media/tais/data/WALOUS/Landcover/Data/fusion_colors.txt"
