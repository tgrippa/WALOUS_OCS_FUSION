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

import grass.script as gscript
import multiprocessing
from multiprocessing import Pool
from functools import partial

def clip(name):
    """ Define a short function for the clip operation """
    global suffix, o, r
    try:
        if r:
            gscript.run_command('r.clip', flags='r', overwrite=o, input=name, output='%s_%s'%(name,suffix))  # With resampling
        else:
            gscript.run_command('r.clip', overwrite=o, input=name, output='%s_%s'%(name,suffix))  # Without resampling
        return "'%s' has been cliped."%name
    except:
        return "ERROR: '%s' has not been cliped. Please check for problem."%name


def clip_multiple_raster(raster_name_list, output_suffix='clip', overwrite=False, resample=False, n_jobs=2):
    """ Define the function to clip a collection of rasters.
    Please be carefull that the clip will be based on region extend and pixels under MASK will be null.
    Please take care of well defining the computational region and a MASK if desired before calling the function.
    """
    global suffix, o, r
    o = overwrite
    r = resample
    suffix = output_suffix

    # Check if i.segment.stats is well installed
    if not gscript.find_program('r.clip', '--help'):
        message = _("You first need to install the addon r.clip.\n")
        message += _(" You can install the addon with 'g.extension r.clip'")
        gscript.fatal(message)

    # Clip the rasters in multiprocessing pool of jobs
    p = Pool(n_jobs)
    output = p.map(clip, raster_name_list)  # Launch the processes for as many items in the list (if function with a return, the returned results are ordered thanks to 'map' function)
    p.close()
    p.join()
    print "\n".join(output)
