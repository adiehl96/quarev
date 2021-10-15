import os, csv, argparse

parser = argparse.ArgumentParser(
    description="quarev: Quartus FPGA Bit Stream Reversal Tool",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
    "path_to_file",
    metavar="PATH",
    default="./data.tff",
    help="path to the file to be bit reversed",
)

args = parser.parse_args()


def bitreverse(n):
    return int("{:08b}".format(n)[::-1], 2)


def open_csv(path_to_file):
    datasetfile = open(path_to_file)
    datasetreader = csv.reader(datasetfile, delimiter=",")
    csv_content = list(datasetreader)
    return csv_content


def process_csv(csv_content):
    return_string = ""
    for row in csv_content:
        for item in row:
            if item.lstrip().isnumeric():
                return_string += str(bitreverse(int(item))).rjust(3) + ","
        return_string += "\n"
    return return_string


full_path = os.path.realpath(args.path_to_file)
csv_content = open_csv(full_path)
return_string = process_csv(csv_content)
print(return_string[:-2], end="")
