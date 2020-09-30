#!/usr/bin/env python

"""
This script is used to store all configuration parameter to run the main code (jupyter notebook)

"""

import os

# Initialize dictionnaries
config_parameters = {}
data = {}


## Please update the following paths according to your own configuration
#config_parameters['PYTHONLIB'] = '/usr/lib/python2.7'
#config_parameters['GISBASE'] = '/usr/lib/grass74'
config_parameters['GRASSBIN'] = '/usr/bin/grass76'
#}config_parameters['GISBASE'] = '/opt/grass'
config_parameters['GISBASE'] = '/usr/lib64/grass76'
#config_parameters['PYTHONLIB'] = '/usr/lib/python2.7' #pour les notebook A, B et C!
config_parameters['PYTHONLIB'] = '/usr/bin/python2.7' # pour le D_predict -- pour executer le fichier R
config_parameters['locationepsg'] = '31370' #  EPSG code for Belgian Lambert 1972
config_parameters['njobs'] = 6 # A CHANGER en fonction de mes besoins

## The following parameters should not be changed normally
config_parameters['gisdb'] = '../GRASSDATA' # path to GRASSDATA folder
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['outputfolder'] = '../fusion/RF_fusion/Results_RW'
config_parameters['location'] = "WALOUS_31370"

## Other folder for automatic output -- NO CHANGE
config_parameters['outputfolder_Logfile'] = os.path.join(config_parameters['outputfolder'],"Log_file")
config_parameters['outputfolder_classfeatures'] = os.path.join(config_parameters['outputfolder'],"Classification_features")
config_parameters['outputfolder_training_sample'] = os.path.join(config_parameters['outputfolder'],"Training_sample")
config_parameters['outputfolder_classifRF'] = os.path.join(config_parameters['outputfolder'],"Classif_RF") #changer ici pour faire des tests avec versions differentes
config_parameters['outputfolder_classifRF_tiles'] = os.path.join(config_parameters['outputfolder_classifRF'],"classif_tiles")
config_parameters['outputfolder_classifRF_csv'] = os.path.join(config_parameters['outputfolder_classifRF'],"classif_csv")
config_parameters['outputfolder_classifRF_valid'] = os.path.join(config_parameters['outputfolder_classifRF'],"test_valid")


## Other path -- NO CHANGE
config_parameters['list_tiles'] = os.path.join(config_parameters['outputfolder'],"list_tiles")
config_parameters['pixel_classes_list'] = os.path.join(config_parameters['outputfolder'],"pixel_classes_list")
config_parameters['rf_trained_model'] = os.path.join(config_parameters['outputfolder_classifRF'],"rf_trained_model.rda")

## The following path linking to datasets should be changed according to your own folder organization
data['tiles'] = ('tiles','../fusion/tuilesRW/FUSION_TUILAGE_ULB_31370.shp')
#data['tiles'] = ('tiles','../fusion/tuilesRW/TUILES_strates47_19miss.shp') # Processing tiles (from OBIA processing) 1er element= nom qui apparaitra dans GRASS, 2eme = CHEMIN vers les donnees
#data['tiles_gpkg_layer'] = 'tuiles' #ligne utile pour geopackage
data['training_points'] = ('training','../RF_fusion/data/points/3000_points_WALOUS_1109_strates.shp')
#data['training_points_gpkg_layer'] = 'batch_1'
#data['validation_points'] = ('validation','../../../Data/points_validation/walous_fusion_pt_validation.gpkg')
data['obia_folder'] = '../OBIA_LC_2018'
data['ortho_lc'] = ('ortho_lc','../entrainement2018/classifs') # 1 m res.
data['senti_lc'] = ('sent_lc','../4Walous/belgium2018_S2/pourclassif/classif_2018_main_rf_LB72_complet.tif') # 10 m res.   #VERSION MAXIMUM LIKELYHOOD
data['senti_croptype'] = ('senti_croptype','../fusion/RF_fusion/data/RW/crop_type/crop2016_type_31370.tif') # 10 m res.
data['binary_crop'] = ('binary_crop','../fusion/RF_fusion/data/RW/crop_mask/crop2016_cm_31370.tif') # 10 m res.
data['binary_agri'] = ('SIGEC','../fusion/RF_fusion/data/RW/sigec/SIGEC_WALLONIE_2018_31370_uint8.tif') # 10 m res.
data['binary_forest'] = ('forest','../fusion/RF_fusion/data/RW/forest/masque_forest_3classes.tif') # 2 m res.
data['binary_hydro'] = ('hydro','../fusion/RF_fusion/data/RW/squelette_eau/Hydro_mask_31370.tif') # 2 m res.
data['binary_roadnet'] = ('roadnet','../fusion/RF_fusion/data/RW/squelette_routes/Roadnet_mask_31370.tif') # 2 m res.
data['binary_built'] = ('built','../fusion/RF_fusion/data/RW/squelette_bati/Buildings_mask_31370.tif') # 1 m res.
data['strata'] =('strata','../fusion/RF_fusion/data/RW/STRATA/')

## Color rule file
data['color_file'] = "/media/tais/data/WALOUS/Data/fusion_colors.txt" # A recevoir de Tais
