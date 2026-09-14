from entry_picker import pick_entry



def delete():
    selected_entry_path = pick_entry()
    if selected_entry_path is None:
        return
    print(f"\n---- Content of {selected_entry_path} ----\n")
    with open(selected_entry_path, "r",) as entry_file:
        print(entry_file.read())
            
    delete_confirmation = input("Are you sure you want to delete this file? (y/n): ")
    if delete_confirmation.lower() == "y":
        selected_entry_path.unlink(missing_ok=True)
        print("Entry deleted successfully!")
    elif delete_confirmation.lower() == "n":
        return
    else:
        print("Invalid choice. Try again later.")