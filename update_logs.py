from entry_picker import pick_entry



def update():
    selected_entry_path = pick_entry()
    if selected_entry_path is None:
        return
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