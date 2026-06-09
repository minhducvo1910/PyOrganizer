'''Cleaner function: turn file into a hash function  (photo.jpg    →  "a3f8c2d...") 
hash: a fingerprint for a file'''

import hashlib

def get_hash(filepath):
    #Create a hasher obj using md5 algorithm
    hasher = hashlib.md5() #Create an empty hasher (no data)

    with open(filepath, "rb") as file:   #NOTE: "rb" (read as byte)
        
        for chunk in iter(lambda: file.read(4096), b""):  #NOTE: read 4096 bytes, not the whole file at one
            hasher.update(chunk)                        #Feed data into hasher obj (file.read read the whole file in raw bytes)
    return hasher.hexdigest()                             #Return hexadecimal characters (0-9, a-f)

def find_duplicate(files):
    seen = {}

    for file in files:
        file_hash = get_hash(file["path"])
        if file_hash in seen:
            seen[file_hash].append(file["path"])   #NOTE: add more path if already in seen (append use for list)
        else:
            seen[file_hash] = [file["path"]]       #Create a new dict ( "a3neu23": ["D:/...", ] (value is a list of path) )
   
    return {h: paths for h, paths in seen.items() if len(paths) > 1}  #NOTE: Only keep the hash with more than 1 paths

