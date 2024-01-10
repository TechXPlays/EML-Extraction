# EML-Extraction
A simple python script to extract email attachments from a large quantity of EML files

<b>Credits</b>
Original Author: Diogo Alves (https://github.com/diogo-alves/eml-extractor)
Me: Editing code to not ask about overwrite but instead just rename

# Features
- Find EML Files (recursively or not) in a selected folder
- Select individual EML files for extraction
- Save all attachments to a single folder
- Organize by email subject in sub folders

# Requirements
Python 3.6+

# Installation
```
Python 3.6+
```
# Usage
By default, the current working directory is used as the source for the EML files, as well as the destination for extracted attachments. You can change this though
```
usage: eml-extractor [OPTIONS]
Extracts attachments from .eml files

optional arguments:
  -h, --help            show this help message and exit
  -s PATH, --source PATH
                        the directory containing the .eml files to extract
                        attachments (default: current working directory)
  -r, --recursive       allow recursive search for .eml files under SOURCE
                        directory
  -f FILE [FILE ...], --files FILE [FILE ...]
                        specify an .eml file or a list of .eml files to extract
                        attachments
  -d PATH, --destination PATH
                        the directory to extract attachments to (default:
                        current working directory)
```

# Examples
**1. Find all .eml files in current working dir, extract the attachments and save them in the same dir:**
```
eml-extractor
```
The command above is equivalent to:
```
eml-extractor --source . --destination .
```
**2. Set another path for searching .eml files:**
```
eml-extractor --source <path>
```
**3. Allow recursive searching:**
```
$ eml-extractor --source /path/to/eml/files/ --recursive
```
# 4. Define manually from which files the attachments will be extracted:
```
$ eml-extractor --files /path/to/file1.eml /path/to/file2.eml
```
# 5. Change the path where to save the extracted attachments:
```
$ eml-extractor --destination /path/to/extracted/attachments/
```
