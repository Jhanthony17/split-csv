# split-csv
This script helps you to split your csv files

Was proved on Windows 10

## Prerequesites
This library uses the following packages from the standard library:
`os`

`argparse`

`csv`

Optionally you can format your code using https://pypi.org/project/black/ which is included in `requirements.txt`

`requirements.txt` is intended to be used with virtual environments https://docs.python.org/3/library/venv.html 

## Usage
`py split_csv.py <name of file to split> <lines you want in each output file>`

You don't need to specify the extension csv.

### Example
`py split_csv.py file_to_split 1000`

That means that the script will split the file 'file_to_split.csv' and it will put 1000 lines in each ouput file.
