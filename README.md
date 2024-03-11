# File hash scraper
This is a Python tool for crawling directories to find and list any files identical by MD5 hash, regardless of filename.

## Installation
Source is available from GitHub and the package is available on pip.

```bash
pip install file-hash-scraper
```

Or user install

```bash
pip install --user file-hash-scraper
```

Or install from GitHub clone.

```bash
git clone https://github.com/eroberson/file_hash_scraper.git
git checkout vN.N.N # Choose highest version tag instead of vN.N.N

pip install .
```

## Usage
```bash
file_hash_scraper --dir d1 --dir d2 --dir d3 --dir d4 > identical_files.txt
```

```bash
file_hash_scraper --dir d1 --loglevel DEBUG 1>identical_files.txt 2>log
```

```bash
file_hash_scraper --dir d1 --readbuffer 4096 > identical_files.txt
```
