PyOrganizer 🗂️
A command-line tool to scan, organize, and clean up files on your computer — built as a final project for CS50P.

Features

📂 Scan a folder and display all files in a sorted, formatted table
🗃️ Organize files automatically into category subfolders (Images, Videos, Documents, etc.)
🔍 Find duplicates by comparing file content using MD5 hashing
🗑️ Delete duplicates safely with confirmation before anything is removed
📝 Logs every action automatically to pyorganizer.log


Installation

Clone the repository:

bashgit clone https://github.com/minhducvo1910/PyOrganizer.git
cd PyOrganizer

Install dependencies:

bashpip install rich

All other libraries (pathlib, shutil, hashlib, argparse, logging) are built into Python — no extra installs needed.


Usage
bash# Scan a folder and display files in a table
python main.py --scan "D:/Downloads"

# Organize files into category subfolders
python main.py --organize "D:/Downloads"

# Find duplicate files
python main.py --duplicate "D:/Downloads"

# Find and delete duplicate files (with confirmation)
python main.py --delete-duplicate "D:/Downloads"

# Show help
python main.py --help

Note: Wrap paths in quotes if they contain spaces.


Example Output
--scan
                  Scanned: D:/Downloads
┌──────────────────┬───────┬─────────┬────────────┐
│ Name             │ Ext   │ Size    │ Modified   │
├──────────────────┼───────┼─────────┼────────────┤
│ homework.pdf     │ .pdf  │ 200 KB  │ 2026-05-03 │
│ notes.txt        │ .txt  │ 1.0 KB  │ 2026-05-10 │
│ photo.jpg        │ .jpg  │ 500 KB  │ 2026-03-02 │
│ video.mp4        │ .mp4  │ 10.0 MB │ 2026-04-20 │
└──────────────────┴───────┴─────────┴────────────┘
--duplicate
Duplicate group:
  D:/Downloads/photo.jpg
  D:/Downloads/photo_copy.jpg

File Categories
Category   |     Extensions
Images     |    .jpg .jpeg .png .gif .webp .svg .heic
Videos     |    .mp4 .mov .avi .mkv .wmv
Music      |    .mp3 .wav .flac .aac .ogg
Documents  |    .pdf .docx .doc .txt .xlsx .pptx .csv
Code       |    .py .js .html .css .json .sql
Programs   |    .exe .msi .dmg .apk .bat
Archives   |    .zip .rar .tar .gz .7z
Fonts      |    .ttf .otf .woff
Others     |    anything not listed above

Project Structure
PyOrganizer/
├── main.py           ← entry point, CLI with argparse
├── Scanner.py        ← scan folders using pathlib
├── Organizer.py      ← move files with shutil
├── Cleaner.py        ← find/delete duplicates with hashlib
├── Logger.py         ← log all actions to pyorganizer.log
├── tests/
│   ├── __init__.py
│   ├── test_scanner.py
│   └── test_cleaner.py
└── README.md

Running Tests
bashpytest tests/

What I Learned
This project was built to go beyond CS50P lectures and explore real-world Python development:
Concept     |  Used For
pathlib     |  Modern file path handling
shutil      |  Moving files safely
hashlib     |  MD5 hashing for duplicate detection
argparse    |  Building a CLI tool with flags
rich        |  Pretty terminal output with tables and colors
logging     |  Persistent action logs with timestamps
pytest      |  Unit testing with temporary directories
Git & GitHub|  Version control and publishing

Author
Minh Duc Vo — CS50P Final Project 2026

GitHub: @minhducvo1910