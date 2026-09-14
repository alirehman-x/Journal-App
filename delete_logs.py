from write_logs import logs_directory
from pathlib import Path


def delete():
    journal_entries = list(logs_directory.glob("*.txt"))
    if not journal_entries:
        print("No files found")
        return
    else:
        journal_entries.sort(reverse=True)
    
    for index, entry_path in enumerate(journal_entries, start=1):
        print(f"[{index}] {entry_path}")

    try:
        user_choice = int(input("Enter the file number you want to delete: "))
        
        if 1 <= user_choice <= len(journal_entries):
            selected_entry_path = journal_entries[user_choice - 1]
            print(f"\n---- Content of {selected_entry_path} ----\n")
            with open(selected_entry_path, "r") as entry_file:
                print(entry_file.read())
            
            delete_confirmation = input("Are you sure you want to delete this file? (y/n): ")
            if delete_confirmation.lower() == "y":
                selected_entry_path.unlink(missing_ok=True)
                print("Entry deleted successfully!")
            elif delete_confirmation.lower() == "n":
                return
            else:
                print("Invalid choice. Try again later.") 

        else:
            print("Invalid choice. Try again later.")
    except ValueError:
        print("Invalid input. Please enter a number.")


delete()
