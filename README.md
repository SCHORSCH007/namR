
# Namer CLI Tool

## Overview
The **Namer CLI Tool** is a command-line utility designed to rename files based on their content or metadata. This tool can be used to automatically organize files in a meaningful way by assigning descriptive names to them, making them easier to search, manage, and work with.

## Supported file-types
- Text-Based Files (TXT, MD, DOCX, PDFs): Use the first few lines, headers, or document metadata to extract key content for naming. These files often contain titles or summaries at the beginning.

- HTML: Parse ```<title>```, headers, and meta tags to generate descriptive filenames.

- Media Files (Images, Audio, Video): Extract metadata (EXIF for images, ID3 for audio, creation date for videos) for renaming. Metadata often includes important details like date, location, or title.

- Code Files (Python, Java, C++): Parse for class names, function names, or comments to derive a meaningful filename.

- Data Files (CSV, Excel): Use headers or the first few rows to create filenames, which often describe the file’s content.

- Structured Files (JSON, XML): Extract key elements like root objects or tag names.

- Ebooks (EPUB, MOBI): Use metadata (title, author) for renaming.


## Features

### 1. File Renamer Based on Text Content
- **Description**: Reads through the file’s text content and generates a meaningful filename based on key aspects (e.g., the title, keywords, or first sentence).
- **Supported File Types**: Text files, Markdown, HTML, code files.
- **How it works**:
  - Extracts content such as the first line, headers, or comments to generate a filename.
  - Allows for custom patterns to be defined by the user.
- **Example**: A text file titled "Project Plan 2024" becomes `project_plan_2024.txt`.

### 2. File Renamer Based on Metadata (For Media Files)
- **Description**: Renames media files based on metadata like EXIF data for images or ID3 tags for audio files.
- **Supported File Types**: Images, videos, audio files.
- **How it works**:
  - For images, it can use metadata like the date taken, location, and camera model.
  - For audio files, it extracts artist, album, and track title.
- **Example**: A photo taken on “2024-09-01” becomes `2024-09-01_paris_trip.jpg`.

### 3. AI-Powered File Naming (For Complex Files)
- **Description**: Uses NLP (Natural Language Processing) or other machine learning techniques to analyze file content and assign descriptive filenames.
- **Supported File Types**: Documents (PDFs, Word files), structured data (CSVs, JSON).
- **How it works**:
  - Summarizes or extracts meaningful keywords from the document to generate a filename.
  - Customizable for different file types.
- **Example**: A document about climate change statistics becomes `climate_change_report_2024.docx`.

### Additional Features

- **File Type Detection**: Automatically detect the type of file and apply different renaming strategies accordingly.
- **Customizable Naming Rules**: Allows users to define naming conventions or patterns (e.g., using specific sections of content or metadata fields).
- **Batch Processing**: Processes multiple files in a directory at once.
- **Dry Run Mode**: Allows users to preview the new filenames before committing to renaming the files.
- **Undo Functionality**: Users can revert to the original filenames after renaming.
- **Integration with Git**: If files are under version control, commits the renaming changes automatically.


## Installation

### For Python Developers
You can run the tool directly from Python:
```bash
pip install namer-cli
namer-cli --help
```

### Building a Standalone Binary
To distribute the tool as a standalone binary (so users don’t need to install Python):
1. Install `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Build the binary:
   ```bash
   pyinstaller --onefile namer-cli.py
   ```
3. The binary will be in the `dist/` folder.

## Usage

```bash
namer-cli rename --directory /path/to/files --type text --pattern "header"
namer-cli rename --file image.jpg --type media --metadata date
namer-cli rename --file script.py --type code --pattern class_name
```

```bash
namer /path/to/file
namer --directory /path/to/dir
namer --pattern (d_t_l, l_d_t) /path/to/file #(only for media files)
namer --setup_api [api_key] #add api key
```

## License
MIT License

## Contributing
Contributions are welcome! Please submit a pull request or file an issue on GitHub.

## Authors
- Your Name
