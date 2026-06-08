'''Scanner function: goes into a folder that the user prompt and comeback with a detail
list of every file inside'''

from pathlib import Path
from datetime import datetime

def scan(directory):
    files = [] #Create an empty file list
    
    p = Path(directory) #Create a p object to use Path() class's function
    if not p.exists():  #Check if folder exist
        raise ValueError("File not exist")
    
    for file in p.iterdir():

        #Check if not subfolder and hidden file
        if file.is_file() and not file.name.startswith("."): 

            #Format the timestampt 
            modified_date = datetime.fromtimestamp(file.stat().st_mtime).strftime("%Y-%m-%d")

            file_info = {
                "path": str(file),
                "name": file.name,
                "extension": file.suffix,     
                "size_bytes": file.stat().st_size,
                "modified_date": modified_date,
            }
            files.append(file_info)
    #Return a files list
    return files
 
