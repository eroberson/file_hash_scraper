#!/usr/bin/env python

"""
file_hash_scraper: a utility for discovering identical files
"""

###########
# imports #
###########
import hashlib
import os
import sys

####################
# Version and name #
####################
__script_path__ = sys.argv[0]
__script_name__ = os.path.basename( __script_path__ )
__version__ = '1.0.0'

#############
# functions #
#############
def BufferedReadMd5Hash( fname, byteLimit = 2 ** 11 ):
	"""Function to read the MD5 hash of a file, using buffering for large files"""

	hasher = hashlib.md5()

	with open( fname, 'rb' ) as infile:
		buf = infile.read( byteLimit )
		while( len( buf ) > 0 ):
			hasher.update( buf )
			buf = infile.read( byteLimit )
	return str( hasher.hexdigest() )

########
# main #
########
if __name__ == "__main__":
	pass
