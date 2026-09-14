from entry_picker import pick_entry



def read():
    selected_entry_path = pick_entry()
    if selected_entry_path is None:
        return
    print(f"\n---- Content of {selected_entry_path} ----\n")
    with open(selected_entry_path, "r") as entry_file:
        print(entry_file.read())