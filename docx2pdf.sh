#!/bin/sh

argnum=$#
if [ $argnum = 0 ]; then
    echo "Converting every file to pdf..."
    python3 docx2pdf.py
elif [ $argnum = 1 ]; then
    echo "Converting $1 to pdf..."
    python3 docx2pdf.py $1
else
    echo "Error: It can only pass one argument."
    exit 0 
fi

echo "Converted Successfully!"
exit 0
