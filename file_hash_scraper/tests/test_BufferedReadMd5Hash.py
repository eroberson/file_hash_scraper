#!/usr/bin/env python

from motif_scraper import BufferedReadMd5Hash

def test_hasher():
	test_file_path = os.path.join( os.path.dirname( __file__ ), '1px.jpeg' )
	correct_hash = '5f51a97d6fb0c9f825c13ee449e70fbe'

	test_hash = BufferedReadMd5Hash( test_file_path, 1024 )

	assert( test_hash == correct_hash )
