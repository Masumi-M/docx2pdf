# from docx2pdf import convert
import sys
from pathlib import Path
import os
from docx2pdf import convert

# Get arguments
args = sys.argv
arg_len = len(args)

# Main program
if arg_len > 1:
    # Execute partially
    file_name = args[1]
    file_name_base = Path(file_name).stem
    convert(file_name, file_name_base+".pdf")
    print("Complete: " + file_name)
else:
    # Execute all
    for file_name in Path('.').rglob('*.docx'):
        convert(str(file_name), file_name.stem+".pdf")
        print("Complete: " + str(file_name))
