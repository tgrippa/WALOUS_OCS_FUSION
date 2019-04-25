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
config_parameters['PYTHONLIB'] = '/usr/lib/python2.7'
config_parameters['locationepsg'] = '31370' #  EPSG code for Belgian Lambert 1972
config_parameters['njobs'] = 6

## The following parameters should not be changed normally
config_parameters['gisdb'] = '../../GRASSDATA' # path to GRASSDATA folder
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['outputfolder'] = '../../../Results'
config_parameters['location'] = "WALOUS_31370"

## The following path linking to datasets should be changed according to your own folder organization 
data['tiles'] = ('tiles','/media/tais/data/WALOUS/Data/obia_2016/tuiles_walous.gpkg') # Processing tiles (from OBIA processing)
data['training_points'] = ('training','../../../Data/points_fusion_all/points_fusion_all.shp')
data['obia_folder'] = '../../../Data/obia_2016'
data['ortho_lc'] = ('ortho_lc','../../../Data/pixel_2016/walous_pixelbassed_2016_raw.tif') # 1 m res.
data['senti_lc'] = ('sent_lc','../../../Data/pixel_2016/rf2016_2dates_SAR_walous_31370.tif') # 10 m res.
data['senti_croptype'] = ('senti_croptype','../../../Data/CropType/crop2016_type_31370.tif') # 10 m res.
data['binary_crop'] = ('binary_crop','../../../Data/CropType/crop2016_cm_31370.tif') # 10 m res.
data['binary_agri'] = ('SIGEC','../../../Data/SIGEC2017/SIGEC2017_mask_31370.tif') # 10 m res.
data['binary_forest'] = ('forest','../../../Data/masque_forestier/masque_forest_31370.tif') # 2 m res.
data['binary_hydro'] = ('hydro','../../../Data/squelette_vectoriel/Hydro_mask_31370.tif') # 2 m res.
data['binary_roadnet'] = ('roadnet','../../../Data/squelette_vectoriel/Roadnet_mask_31370.tif') # 2 m res.
data['binary_built'] = ('built','../../../Data/squelette_vectoriel/Buildings_mask_31370.tif') # 1 m res.
