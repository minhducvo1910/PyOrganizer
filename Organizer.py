'''Organizer: Take result from scan(), organize files and move files into organized subfolder'''
import shutil
from pathlib import Path

Categories ={
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".xls": "Documents",
    ".pptx": "Documents",
    ".ppt": "Documents",
    ".csv": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".webp": "Images",
    ".ico": "Images",

    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",

    # Music
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".aac": "Music",
    ".ogg": "Music",

    # Code
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".java": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".json": "Code",
    ".xml": "Code",
    ".sql": "Code",

    # Executables / Programs
    ".exe": "Programs",
    ".msi": "Programs",
    ".dmg": "Programs",
    ".apk": "Programs",
    ".bat": "Programs",
    ".sh": "Programs",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".7z": "Archives",

    # Fonts
    ".ttf": "Fonts",
    ".otf": "Fonts",
    ".woff": "Fonts",
}
def organize(files):
    for file in files:
        
        #Find the category
        category = Categories.get(file["extension"].lower(), "Others") #Get retrun default if key doesn't exist

        #Create the destination folder path
        destination_folder = Path(file["path"]).parent / category  #The "/" in pathlib join paths

        #Create folder and move file
        destination_folder.mkdir(exist_ok=True)
        shutil.move(file["path"], destination_folder / file["name"])