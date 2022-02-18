#split-csv
This script helps you to split your csv files

Was proved on Windows 10

## Prerequesites
`You'll need to install the follow packeage with pip:
os
argparse
csv`

## Usage
`python split_csv.py <name of file to split> <lines you want in each output file>`

You don't need to specify the extension csv.

### Example
`python split_csv.py file_to_split 1000`

That means that the script will split the file 'file_to_split.csv' and it will put 1000 lines in each ouput file.
