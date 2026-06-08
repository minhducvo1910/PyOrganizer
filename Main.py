'''Main function: CLI(Command line interface): user use program by typing in the terminal'''
'''Example: python main.py --scan "C:/Users/You/Downloads"
            python main.py --organize "C:/Users/You/Downloads"
    That --scan, --organize etc. are called flags or arguments'''

import argparse
from Scanner import scan
from Organizer import organize

def main():
    parser = argparse.ArgumentParser(description="PyOrganizer - File Managemnet Tool")
    parser.add_argument("--scan", metavar="FOLDER", nargs="+", help= "Scan a folder and list files")

    parser.add_argument("--organize", metavar="FOLDER", nargs="+", help= "Organize a folder")

    args = parser.parse_args()  #Read user input in the command line after main.py

    #NOTE: Organize path
    scan_folder = " ".join(args.scan) if args.scan else None                #Join words with space
    organize_folder = " ".join(args.organize) if args.organize else None

    if args.scan:
       
        try:
            results = scan(scan_folder)
            for result in results:
                print(result)
        except ValueError as e:
            print(f"Error: {e}")
    elif args.organize:
        try:
            results = scan(organize_folder)
            organize(results)
        except ValueError as e:
            print(F"Error: {e}")
    else:
        parser.print_help()
    
    


if __name__ == "__main__":
    main()
