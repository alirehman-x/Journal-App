from write_logs import target_directory
from pathlib import Path


def update():
    logs_files = list(target_directory.glob("*.txt"))
    if not logs_files:
        print("No files found")
        return
    else:
        logs_files.sort(reverse=True)
    for index, log_file in enumerate(logs_files, start=1):
        print(f"[{index}] {log_file}")

    try:
        choice = int(input("Enter the file number you want to open: "))
        
        if 1 <= choice <= len(logs_files):
            selected_file = logs_files[choice - 1]
            print(f"\n---- Content of {selected_file} ----\n")
            with open(selected_file, "r") as file:
                print(file.read())
            choice2 = input("would you like to edit the file y/n ")
            if choice2 == "y":
                updated_data = input("Enter the text you want to append: ")
                with open(selected_file, "a") as file:
                    file.write(updated_data)
            elif choice2 == "n":
                return
            else:
                print(" Invalid choice Try again later ") 

        else:
            print(" Invalid choice Try again later ")
    except ValueError:
        print("Invalid Input")


update()
