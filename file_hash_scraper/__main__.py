#!/usr/bin/env python

###########
# imports #
###########
import argparse
import hashlib
import logging
import os
import shutil
import sys

###################################
# import from initialization file #
###################################
from file_hash_scraper import __script_name__, __version__, BufferedReadMd5Hash

def run():
	#############
	# arg parse #
	#############
	parser = argparse.ArgumentParser( prog = __script_name__, epilog = "%s v%s" % ( __script_name__, __version__ ) )

	parser.add_argument( "--dir", help = "Directory to scan (can be specified multiple times)", action = 'append' )
	parser.add_argument( "--readbuffer", help = "Size of the buffer used for hashing (bytes). Larger buffers may be faster for large files.", type = int, default = 2 ** 11 )
	parser.add_argument( "--loglevel", choices = [ 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' ], default = 'INFO' )

	input_args = parser.parse_args()

	#################
	# setup logging #
	#################
	logging.basicConfig( format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' )
	logger = logging.getLogger( __script_name__ )
	logger.setLevel( input_args.loglevel )

	################
	# dir validity #
	################
	if input_args.dir is None:
		logger.error( "No input directories specified" )
		sys.exit( 1 )

	if len( input_args.dir ) == 0:
		logger.error( "No input directories specified" )
		sys.exit( 1 )

	############################
	# Can't read with 0 buffer #
	############################
	if not input_args.readbuffer > 0:
		logger.error( "Read buffer must be greater than 0" )
		sys.exit( 1 )

	#######################
	# setup dirs to crawl #
	#######################
	dirs_to_crawl = []
	for directory in input_args.dir:
		current_dir = os.path.normpath( directory )
		if current_dir not in dirs_to_crawl:
			dirs_to_crawl.append( current_dir )

	############################
	# Tracking for file hashes #
	############################
	hash_dict = {}

	###################
	# Get to crawling #
	###################
	for walking_dir in dirs_to_crawl:
		for root, dirs, files in os.walk( walking_dir, topdown = False ):
			for fname in files:
				fpath = os.path.join( root, fname )

				logger.debug( "file: %s" % ( fname ) )
				logger.debug( "path: %s" % ( fpath ) )

				#####################################
				# don't waste time with empty files #
				#####################################
				if not os.path.getsize( fpath ) > 0:
					logger.debug( "Empty file [%s]" % ( fpath ) )
					continue

				file_hash = BufferedReadMd5Hash( fpath, input_args.readbuffer )

				if file_hash in hash_dict:
					if fpath in hash_dict[ file_hash ]:
						continue
					else:
						hash_dict[ file_hash ].append( fpath )
				else:
					hash_dict[ file_hash ] = [ fpath, ]

	################################
	# check all hashes             #
	# write any present >= 2 times #
	################################
	print( 'hash\tpath' )
	for key in hash_dict:
		if len( hash_dict[ key ] ) > 1:
			for fpath in hash_dict[ key ]:
				print( '%s\t%s' % ( key, fpath ) )

if __name__ == "__main__":
	run()
