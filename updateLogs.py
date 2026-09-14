from writeLogs import targetDirectory
from pathlib import Path


def update():
     journal_entries = list(targetDirectory.glob("*.txt"))
     if not journal_entries:
         print("No files found")
         return
     else:
         journal_entries.sort(reverse=True)
     
     for index, entry_path in enumerate(journal_entries, start=1):
         print(f"[{index}] {entry_path}")

     try:
         user_choice = int(input("Enter the file number you want to open: "))
         
         if 1 <= user_choice <= len(journal_entries):
             selected_entry_path = journal_entries[user_choice - 1]
             print(f"\n---- Content of {selected_entry_path} ----\n")
             with open(selected_entry_path, "r") as entry_file:
                 print(entry_file.read())
             
             edit_confirmation = input("Would you like to edit the file? (y/n): ")
             if edit_confirmation.lower() == "y":
                 additional_content = input("Enter the text you want to append: ")
                 with open(selected_entry_path, "a") as entry_file:
                     entry_file.write(additional_content)
                 print("Entry updated successfully!")
             elif edit_confirmation.lower() == "n":
                 return
             else:
                 print("Invalid choice. Try again later.") 

         else:
             print("Invalid choice. Try again later.")
     except ValueError:
         print("Invalid input. Please enter a number.")


update()
