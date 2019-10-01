#!/usr/bin/env python

"""
Functions for automatic check and creation of folders
"""

import os

def check_create_dir(path, quiet=False):
	if os.path.exists(path):
	    if not quiet: print "The folder '%s' already exists"%path 
	else: 
		os.makedirs(path) 
		if not quiet: print "The folder '%s' has been created"%path
		
#Test ATOM auto-fetch
