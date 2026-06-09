'''Logger: keep track of every action that the program take into a log file'''

import logging
from datetime import datetime

logging.basicConfig(
    filename = "PyOrganizer.log",
    level = logging.INFO, 
    format="%(asctime)s - %(message)s"
)

def log_scan(folder, file_count):
    logging.info(f"SCAN - Scanned folder: {folder} - {file_count} files found")

def log_organize(filename, destination):
    logging.info(f"ORGANIZE - Moved {filename} to {destination}")

def log_duplicate(folder, group_count):
    logging.info(f"FIND DUPLICATE -  Found {group_count} duplications in {folder}")

def log_deletion(deleted_path, original_path):
    logging.info(f"DELETED {deleted_path} - duplicated of {original_path}")