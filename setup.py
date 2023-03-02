from setuptools import setup

setup(
	name = "file_hash_scraper",
	packages = ['file_hash_scraper'],
	version = "1.0.0",
	description = 'This utility scans directories recursively, hashes all files, and reports the path of any files that have identical MD5 hashes.',
	author = "Elisha Roberson",
	author_email = 'dr.eli.roberson@gmail.com',
	url = 'https://github.com/eroberson/file_hash_scraper',
	license = 'MIT',
	classifiers=[
	"Development Status :: 5 - Production/Stable",
	"Environment :: Console",
	"License :: OSI Approved :: MIT License",
	"Topic :: Utilities",
	"Programming Language :: Python :: 2.7",
	"Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.7",
	"Programming Language :: Python :: 3.8",
	"Programming Language :: Python :: 3.9",
	"Programming Language :: Python :: 3.10",
	"Programming Language :: Python :: 3.11"
	],
	keywords='Utility for scanning for identical files by MD5 hash',
	entry_points = {'console_scripts':["file_hash_scraper = file_hash_scraper.__main__:run"]},
	test_suite = 'nose.collector',
	tests_require = ['nose']
)
