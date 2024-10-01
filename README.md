
# Namer CLI Tool

## Overview
The **Namer CLI Tool** is a command-line utility designed to rename files based on their content or metadata.


## Features

### 1. File Renamer Based on Metadata (For picture Files)
- **Description**: Renames to YYYY-MM-DD_HH-MM-SS_<Description_if_given>
- **Supported File Types**:['.jpg', '.jpeg','.cr2', '.nef', '.arw', '.dng']

### 2. AI-Powered File Naming (For Complex Files)
- **Description**: Uses the googel gemini ai to autoname Docx-files
- **Supported File Types**: Docx (for now)
- **How it works**:
  - promts the first 100 words of the document and metadata to the AI and it returns the filename
- **Example**: A document about climate change statistics becomes `climate_change_report_2024.docx`.



## Preperation

```bash
export GOOGLE_API_KEY="<API_KEY>"
```

## Usage

```bash
usage: parser.py [-h] [-f] [-r] [-d DESCRIPTION] path [path ...]

Namr: Automatically rename your files.

positional arguments:
  path                  Path for Namr to process files. Wildcards and directories are accepted.

options:
  -h, --help            show this help message and exit
  -f, --force           Rename files without confirmation.
  -d DESCRIPTION, --description DESCRIPTION
                        Rename supported Pictures with a given description to YYYY-MM-DD_HH-MM-SS_<Description> on other file formats this
                        will be given to the AI
```

## Confirmation

```bash
"testing/Text comprehension and analysis.docx" will be named "testing/Wikipedia_Success_Media_Landscape.docx", proceed? [y,n] 
```

## License
MIT License

## Contributing
Contributions are welcome! Please submit a pull request or file an issue on GitHub.

## Authors
- Your Name
