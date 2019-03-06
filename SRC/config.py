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
config_parameters['locationepsg'] = '31370' #  EPSG code for Belgian Lambert 1972
config_parameters['njobs'] = 8

## The following parameters should not be changed normally
config_parameters['gisdb'] = '../../GRASSDATA' # path to GRASSDATA folder
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['outputfolder'] = '../../Results'

## The following path linking to datasets should be changed according to your own folder organization 
data['training_points'] = '../../../Data/points_fusion/points_fusion_1500.gpkg'
data['obia_folder'] = '../../../Results/obia_2016/HERVE'
data['pix_orth'] = '../../../Results/pixel_2016/walous_pixelbassed_2016_raw.tif'
data['pix_senti'] = '../../../Results/pixel_2016/rf2016_2dates_SAR_walous.tif'

