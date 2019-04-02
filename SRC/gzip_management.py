#!/usr/bin/env python

"""
Functions for compression and decompressing gzip files
http://xahlee.info/python/gzip.html

"""

import gzip

def decompress_gzip(in_path, out_path):
	inF = gzip.GzipFile(in_path, 'rb')
	s = inF.read()
	inF.close()

	outF = file(out_path, 'wb')
	outF.write(s)
	outF.close()
	
def compress_gzip(in_path, out_path):
	inF = file(in_path, 'rb')
	s = inF.read()
	inF.close()

	outF = gzip.GzipFile(out_path, 'wb')
	outF.write(s)
	outF.close()