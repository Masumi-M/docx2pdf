# docx2pdf

=====

## Description

- Shell command project to convert the docx files in the current directory to pdf.

## Requirement

- macOS
- Python3
- Python Package ([docx2pdf](https://pypi.org/project/docx2pdf/))

## Setup

```zsh:setup.sh
% pip3 install docx2pdf
% chmod 755 ./docx2pdf
```

## Usage

### 1. Dump in Word File (docx)

Dump in the word file to the current directory like the `sample.docx`.

### 2. Execute the Command (All)

Execute the next command to convert every file in the current directory.

```zsh:execute.sh
% ./docx2pdf
```

### 3. Execute the Command (Partial)

Execute the next command to convert the specified file.

```zsh:execute.sh
% ./docx2pdf sample.docx
```

## Author

- [Masumi Morishige](https://www.umi-mori.jp)
