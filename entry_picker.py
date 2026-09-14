from write_logs import logs_directory


def pick_entry(prompt="Enter the file number you want to open: "):
    journal_entries = list(logs_directory.glob("*.txt"))
    if not journal_entries:
        print("No files found")
        return None

    journal_entries.sort(reverse=True)
    for index, entry_path in enumerate(journal_entries, start=1):
        print(f"[{index}] {entry_path}")

    try:
        user_choice = int(input(prompt))
        if 1 <= user_choice <= len(journal_entries):
            return journal_entries[user_choice - 1]
        else:
            print("Invalid choice. Try again later.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None