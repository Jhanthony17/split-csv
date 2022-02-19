import os
import argparse

parser = argparse.ArgumentParser(
    description="Necesary Arguments:",
    epilog="This an example to use it: py scrip_split_csv.py 'file_to_split.csv' 1000",
)

parser.add_argument(
    "name_csv", metavar="[-Name]", type=str, help="Name of the csv to split"
)
parser.add_argument(
    "lines",
    metavar="[-Lines]",
    type=int,
    help="Number of lines you want in each output file",
)
args = parser.parse_args()
file = args.name_csv
file2 = "vulns"


def split(
    filehandler,
    delimiter=",",
    row_limit=args.lines,
    output_name_template="output_%s.csv",
    output_path=".",
    keep_headers=True,
):

    import csv

    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(output_path, output_name_template % current_piece)

    class MyDialect(csv.Dialect):
        delimiter = ","
        quotechar = '"'
        doublequote = True
        skipinitialspace = False
        lineterminator = "\n"
        quoting = csv.QUOTE_MINIMAL

    current_out_writer = csv.writer(open(current_out_path, "w"), MyDialect())
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path, output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, "w"), MyDialect())
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)


split(open(f"{file}.csv", "r"))
