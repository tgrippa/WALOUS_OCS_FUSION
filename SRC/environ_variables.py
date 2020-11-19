#!/usr/bin/env python

"""
Functions related to environmental variables
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

import os,sys
from __main__ import config_parameters


def setup_environmental_variables():
	"""	Setting the environment variables allowing to use of GRASS GIS python libraries 
	Documentaion available on: https://grass.osgeo.org/grass64/manuals/variables.html
	Please change the directory path according to your own system configuration.
	Here after are the path used on a LINUX UBUNTU Mint 18.1 (Serena).
    """
	# Check is environmental variables exists and create them (empty) if not exists.
	if not 'PYTHONPATH' in os.environ:
		os.environ['PYTHONPATH']=''
	if not 'LD_LIBRARY_PATH' in os.environ:
		os.environ['LD_LIBRARY_PATH']=''
	# Set environmental variables
	os.environ['GISBASE'] = config_parameters['GISBASE']
	os.environ['GRASSBIN'] = config_parameters['GRASSBIN']
	os.environ['PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'bin')
	os.environ['PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'scripts')
	os.environ['PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'lib')
	os.environ['PYTHONPATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'etc','python')
	os.environ['PYTHONPATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'etc','python','grass')
	os.environ['PYTHONPATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'etc','python','grass','script')
	os.environ['PYTHONLIB'] = config_parameters['PYTHONLIB']
	os.environ['LD_LIBRARY_PATH'] += os.pathsep + os.path.join(os.environ['GISBASE'],'lib')
	os.environ['GIS_LOCK'] = '$$'
	os.environ['GISRC'] = os.path.join(os.environ['HOME'],'.grass7','rc')  ## Guess will only works for LINUX

	## Define GRASS-Python environment
	#sys.path.append(os.path.join(os.environ['GISBASE'],'etc','python'))


def print_environmental_variables():
	"""
	Display the current environmental variables of your computer.
	"""
	## Display the current defined environment variables
	for key in os.environ.keys():
		print ("%s = %s \t" % (key,os.environ[key]))