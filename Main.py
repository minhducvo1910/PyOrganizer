'''Main function: CLI(Command line interface): user use program by typing in the terminal'''
'''Example: python main.py --scan "C:/Users/You/Downloads"
            python main.py --organize "C:/Users/You/Downloads"
    That --scan, --organize etc. are called flags or arguments'''

import argparse
from rich.console import Console
from rich.table import Table 
from Scanner import scan
from Organizer import organize
from Cleaner import  find_duplicate, delete_duplicate
from logger import log_scan, log_duplicate

console = Console()
def main():
    parser = argparse.ArgumentParser(description="PyOrganizer - File Managemnet Tool")
    parser.add_argument("--scan", metavar="FOLDER", nargs="+", help= "Scan a folder and list files")

    parser.add_argument("--organize", metavar="FOLDER", nargs="+", help= "Organize a folder")

    parser.add_argument("--duplicate", metavar="FOLDER", nargs="+", help="Find any duplicate files")

    parser.add_argument("--delete-duplicate", metavar="FOLDER", nargs="+", help= "Delete any duplications")

    args = parser.parse_args()  #Read user input in the command line after main.py

    #NOTE: Organize path
    scan_folder = " ".join(args.scan) if args.scan else None                #Join words with space
    organize_folder = " ".join(args.organize) if args.organize else None
    duplicate_folder = " ".join(args.duplicate) if args.duplicate else None
    delete_duplicate_folder = " ".join(args.delete_duplicate) if args.delete_duplicate else None

    #Call scan function
    if args.scan:
        try:
            results = scan(scan_folder)
            log_scan(scan_folder, len(results))   #NOTE: track the event in log file

            #Sorted date
            sorted_result = sorted(results,
                                key=lambda f: (f["extension"], -f["size_bytes"], f["modified_date"]),
            )

            #Rich table
            table = Table(title=f"Scanned: {scan_folder}")
            table.add_column("Name", style="cyan")
            table.add_column("Extension", style="green")
            table.add_column("Size (bytes)", style="yellow")
            table.add_column("Modified date", style="magenta")

            #Print table
            for result in sorted_result:
                table.add_row(
                    result["name"],
                    result["extension"],
                    str(result["size_bytes"]),
                    result["modified_date"]
                )
            console.print(table)
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")

    #Call organize function
    elif args.organize:
        try:
            results = scan(organize_folder)
            organize(results)
            console.print(f"[green]Succesfully organized {len(results)} files![/green]")
        except ValueError as e:
            print(f"Error: {e}")

    #Call find_duplicate function
    elif args.duplicate:
        try:
            results = scan(duplicate_folder)
            duplicate_file = find_duplicate(results)
            if duplicate_file:
                log_duplicate(duplicate_folder, len(duplicate_file))
                for _, paths in duplicate_file.items():
                    console.print(f"\n[yellow]Duplicate group:[/yellow] ")
                    for path in paths:
                        console.print(f"  [red]{path}[/red]")
            else:
                console.print("[green]No duplicate found![/green]")
            
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
    
    #Delete any dupicate
    elif args.delete_duplicate:
        try:
            results = scan(delete_duplicate_folder)
            duplicates = find_duplicate(results)
            if duplicates:
                delete_duplicate(duplicates)
                console.print(f"[green]Successfully deleted {len(duplicates)} duplicate groups![/green]")
            else:
                print(f"No duplicate found!")
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")


    else:
        parser.print_help()


if __name__ == "__main__":
    main()

