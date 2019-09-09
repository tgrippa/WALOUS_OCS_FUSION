#!/usr/bin/env python

"""
This script is used to store all configuration parameter to run the main code (jupyter notebook)

"""

import os

# Initialize dictionnaries
config_parameters = {}
data = {}


## Please update the following paths according to your own configuration
config_parameters['GISBASE'] = '/usr/lib/grass76'
#config_parameters['PYTHONLIB'] = '/usr/lib/python2.7'
config_parameters['PYTHONLIB'] = '/usr/bin/python2'
config_parameters['locationepsg'] = '31370' #  EPSG code for Belgian Lambert 1972
config_parameters['njobs'] = 6

## The following parameters should not be changed normally
config_parameters['gisdb'] = '../../GRASSDATA' # path to GRASSDATA folder
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['outputfolder'] = '../../../Postprocess_V1'
config_parameters['location'] = "WALOUS_31370"

## Other folder for automatic output
config_parameters['outputfolder_Logfile'] = os.path.join(config_parameters['outputfolder'],"Log_file")
config_parameters['outputfolder_Raster'] = os.path.join(config_parameters['outputfolder'],"Raster")
config_parameters['outputfolder_Vecteur'] = os.path.join(config_parameters['outputfolder'],"Vecteur")


## Other path
config_parameters['list_tiles'] = os.path.join(config_parameters['outputfolder'],"list_tiles")

## The following path linking to datasets should be changed according to your own folder organization
data['tiles'] = ('tiles','/media/tais/data/WALOUS/Landcover/tiles_marche.shp') # Processing tiles
data['fusion_folder'] = '../../../Results_V2/Classif_RF_All_points/classif_tiles'
data['binary_agri'] = ('SIGEC','../../../Data/SIGEC2017/SIGEC2017_mask_31370.tif') # 10 m res.
data['binary_forest'] = ('forest','../../../Data/masque_forestier/masque_forest_31370.tif') # 2 m res.
data['binary_hydro'] = ('hydro','../../../Data/squelette_vectoriel/Hydro_mask_31370.tif') # 2 m res.
data['binary_roadnet'] = ('roadnet','../../../Data/squelette_vectoriel/Roadnet_mask_31370.tif') # 2 m res.
data['binary_built'] = ('built','../../../Data/squelette_vectoriel/Buildings_mask_31370.tif') # 1 m res.
data['binary_rail'] = ('rail','../../../Data/squelette_vectoriel/rail.tif') # 1 m res.

## Color rule file
data['color_file'] = "/media/tais/data/WALOUS/Landcover/Data/fusion_colors.txt"
