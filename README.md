# Journal App

A simple Python-based command-line journal application for writing, reading, and updating personal journal entries.

## Overview

Journal App is a lightweight tool that allows you to:
- **Write** new journal entries with automatic timestamps
- **Read** previously written entries in a user-friendly interface
- **Update** existing journal entries

Each entry is saved as a text file with a timestamp in the filename, making it easy to organize and find past entries.

## Features

- ✍️ **Write Entries**: Quickly write what's on your mind with automatic date and time stamping
- 📖 **Read Entries**: Browse and view all previously written journal entries
- ✏️ **Update Entries**: Edit and update existing journal entries
- 📁 **Organized Storage**: Entries are stored in a dedicated directory with timestamp-based filenames
- 🖥️ **Simple CLI Interface**: Easy-to-use command-line interface

## Project Structure

```
Journal-App/
├── writeLogs.py      # Module for creating new journal entries
├── readLogs.py       # Module for reading existing journal entries
├── updateLogs.py     # Module for updating existing journal entries
├── .gitignore        # Git ignore rules for Python projects
└── README.md         # Project documentation
```

## Files

### `writeLogs.py`
Handles creating new journal entries. 
- Prompts user to input their thoughts
- Automatically creates a timestamped text file
- Saves entries to `D:/Docs/Code/Python/Logs` directory (configurable)
- File naming format: `Entry YYYY_MM_DD HH-MM-SS.txt`

### `readLogs.py`
Handles reading and displaying journal entries.
- Lists all available journal entries sorted by most recent first
- User selects an entry by number to read its content
- Displays the full content of the selected entry
- Includes error handling for invalid inputs

### `updateLogs.py`
Handles updating existing journal entries.
- Displays a list of all available entries
- User selects an entry by number to edit
- Allows modification of selected entry content
- Saves changes to the same timestamped file

## Usage

### Writing a Journal Entry

Run the write module:
```bash
python writeLogs.py
```

You will be prompted:
```
Write what is on your mind: 
```

Enter your thoughts and press Enter. Your entry will be saved with a timestamp.

### Reading Journal Entries

Run the read module:
```bash
python readLogs.py
```

A list of all entries will be displayed:
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
python updateLogs.py
```

A list of all entries will be displayed. Select an entry number to edit it, make your changes, and the entry will be updated.

## Configuration

The default logs directory is set to `D:/Docs/Code/Python/Logs`. To change this, modify the `targetDirectory` variable in `writeLogs.py`:

```python
targetDirectory = Path("your/custom/path/here")
```

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## Future Enhancements

- [ ] Add delete functionality for entries
- [ ] Add search/filter capabilities
- [ ] Add tags or categories for entries
- [ ] Add export to different formats (PDF, JSON, etc.)
- [ ] GUI interface option

## License

This project is open source and available for personal use.
