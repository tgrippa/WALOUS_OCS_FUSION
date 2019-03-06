#!/usr/bin/env python

"""
This script is used to store all configuration parameter to run the main code (jupyter notebook)

"""

import os

# Initialize dictionnaries
config_parameters = {}
data = {}
rule_file = {}
roads_veloc = {}

## Please update the following paths according to your own configuration 
config_parameters['GISBASE'] = '/home/tais/SRC/GRASS/grass_trunk/dist.x86_64-pc-linux-gnu'
config_parameters['PYTHONLIB'] = '/usr/lib/python2.7'
config_parameters['locationepsg'] = '32628' #  EPSG code for WGS84 UTM ZONE 28N (SENEGAL)
config_parameters['njobs'] = 3
config_parameters['resolution'] = '100'

## The following parameters should not be changed normally
config_parameters['gisdb'] = '../GRASSDATA' # path to GRASSDATA folder
config_parameters['location'] = 'shedecides'  # name of the location (existing or for a new one)
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['outputfolder'] = '../Results/SEN'
config_parameters['time_limits'] = ('30','60','120','240','360','480','4800000')  # time limits for isochrones (in minutes)

## The following path linking to datasets should not be changed normally
data['admin'] = ('admin1','../Data/Admi/SEN_adm1.shp')
data['WOCBA_PPP'] = ('WOCBA_PPP','../Data/SEN/ppp_prj_2014_SEN_WOCBA.tif')
data['POP_PPP'] = ('POP_PPP','../Data/SEN/ppp_prj_2014_SEN.tif')
data['WOCBA_PPH'] = 'WOCBA'
data['POP_PPH'] = 'POP'
data['LULC'] = ('LULC','../Data/Globcover/LC_sen.tif')
data['ROADS'] = ('ROADS','../Data/Roads/SEN_roads.shp')
data['HC'] = ('HC','../Data/facilities_senegal.csv')

## The following path linking to rule files should not be changed normally
rule_file['Velocity_LULC'] = '../Data/Velocity_LULC'
rule_file['globcover_WS'] = "../Data/Globcover/reclass_globcover_WS"
rule_file['globcover_DS'] = "../Data/Globcover/reclass_globcover_DS"
	
## Values for velocity for roads
roads_veloc["WC"] = "17"
roads_veloc["NC"] = "120"