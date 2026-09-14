# Journal App

A simple Python-based command-line journal application for writing, reading, updating, and deleting personal journal entries.

## Overview

Journal App is a lightweight tool that allows you to:
- **Write** new journal entries with automatic timestamps
- **Read** previously written entries in a user-friendly interface
- **Update** existing journal entries by appending new content
- **Delete** journal entries you no longer need

Each entry is saved as a text file with a timestamp in the filename, making it easy to organize and find past entries.

## Features

- ✍️ **Write Entries**: Quickly write what's on your mind with automatic date and time stamping
- 📖 **Read Entries**: Browse and view all previously written journal entries
- ✏️ **Update Entries**: Edit and append to existing journal entries
- 🗑️ **Delete Entries**: Remove journal entries you no longer need
- 📁 **Organized Storage**: Entries are stored in a dedicated directory with timestamp-based filenames
- 🖥️ **Simple CLI Interface**: Easy-to-use command-line interface

## Project Structure

```
Journal-App/
├── write_logs.py      # Module for creating new journal entries
├── read_logs.py       # Module for reading existing journal entries
├── update_logs.py     # Module for updating existing journal entries
├── delete_logs.py     # Module for deleting journal entries
├── .gitignore         # Git ignore rules for Python projects
└── README.md          # Project documentation
```

## Files

### `write_logs.py`
Handles creating new journal entries. 
- Prompts user to input their thoughts
- Automatically creates a timestamped text file
- Saves entries to `D:/Docs/Code/Python/Logs` directory (configurable)
- File naming format: `Entry YYYY_MM_DD HH-MM-SS.txt`

### `read_logs.py`
Handles reading and displaying journal entries.
- Lists all available journal entries sorted by most recent first
- User selects an entry by number to read its content
- Displays the full content of the selected entry
- Includes error handling for invalid inputs

### `update_logs.py`
Handles updating existing journal entries.
- Displays a list of all available entries sorted by most recent first
- User selects an entry by number to view and edit
- Shows the current content of the selected entry
- Allows appending new text to the selected entry
- Saves changes to the same timestamped file

### `delete_logs.py`
Handles deleting journal entries.
- Displays a list of all available entries sorted by most recent first
- User selects an entry by number to delete
- Shows the entry content before deletion for confirmation
- Requires user confirmation before permanently deleting the entry
- Uses safe deletion with error handling

## Usage

### Writing a Journal Entry

Run the write module:
```bash
python write_logs.py
```

You will be prompted:
```
Write what is on your mind: 
```

Enter your thoughts and press Enter. Your entry will be saved with a timestamp.

### Reading Journal Entries

Run the read module:
```bash
python read_logs.py
```

A list of all entries will be displayed (sorted by most recent first):
```
[1] Entry 2024_09_13 14-30-45.txt
[2] Entry 2024_09_12 09-15-20.txt
...
Enter the file number you want to open: 
```

Enter the number of the entry you want to read.

### Updating Journal Entries

Run the update module:
```bash
python update_logs.py
```

A list of all entries will be displayed. Select an entry number to view it, then choose whether to append additional content to that entry.

```
[1] Entry 2024_09_13 14-30-45.txt
...
Enter the file number you want to open: 1

---- Content of Entry 2024_09_13 14-30-45.txt ----
[Current entry content]

Would you like to edit the file? (y/n): y
Enter the text you want to append: [Additional content]
Entry updated successfully!
```

### Deleting Journal Entries

Run the delete module:
```bash
python delete_logs.py
```

A list of all entries will be displayed. Select an entry number to view and delete it:

```
[1] Entry 2024_09_13 14-30-45.txt
...
Enter the file number you want to delete: 1

---- Content of Entry 2024_09_13 14-30-45.txt ----
[Entry content]

Are you sure you want to delete this file? (y/n): y
Entry deleted successfully!
```

## Configuration

The default logs directory is set to `D:/Docs/Code/Python/Logs`. To change this, modify the `logs_directory` variable in `write_logs.py`:

```python
logs_directory = Path("your/custom/path/here")
```

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## Future Enhancements

- [ ] Add search/filter capabilities
- [ ] Add tags or categories for entries
- [ ] Add export to different formats (PDF, JSON, etc.)
- [ ] Create a unified menu interface (instead of separate scripts)
- [ ] GUI interface option
- [ ] Add entry date modification capabilities

## License

This project is open source and available for personal use.
