'''Main function: CLI(Command line interface): user use program by typing in the terminal'''
'''Example: python main.py --scan "C:/Users/You/Downloads"
            python main.py --organize "C:/Users/You/Downloads"
    That --scan, --organize etc. are called flags or arguments'''

import argparse
from Scanner import scan

def main():
    parser = argparse.ArgumentParser(description="PyOrganizer - File Managemnet Tool")
    parser.add_argument("--scan", metavar="FOLDER", nargs="+", help= "Scan a folder and list files")
    args = parser.parse_args()  #Read user input in the command line after main.py

    if args.scan:
        folder = " ".join(args.scan)  #Join words with space
        try:
            results = scan(folder)
            for result in results:
                print(result)
        except ValueError as e:
            print(f"Error: {e}")
    else:
        parser.print_help()
        

if __name__ == "__main__":
    main()
