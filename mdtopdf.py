import argparse
import os
import subprocess
import sys

cwd = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(
    prog="mdtopfd",
    description="Convert and concatenate markdown files to good looking pdf file",
)
parser.add_argument(
    "-concat",
    action="extend",
    nargs="+",
    type=str,
    help="consecutive files or a .txt file",
)
parser.add_argument("-raw", action="store_true", help="raw pandoc conversion")
parser.add_argument("-edithead", action="store_true", help="open head.tex")
parser.add_argument(
    "-o", default="out.pdf", help="file name of output, defaults to out.pdf"
)
args = parser.parse_args()

if args.edithead:
    subprocess.run(["head.tex"], shell=True)
    sys.exit()

if args.raw:
    raw_option = []
else:
    raw_option = ["-H", "head.tex"]

if len(args.concat) == 1:
    with open(args.concat[0]) as f:
        filenames = f.read().split("\n")
    args.concat = [x.replace('"', "") for x in filenames if len(x) > 0]

subprocess.run(["pandoc", "-s"] + args.concat + raw_option + ["-o", args.o])
