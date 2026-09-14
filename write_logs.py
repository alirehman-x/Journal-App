from datetime import datetime
from pathlib import Path


logs_directory = Path("D:/Docs/Code/Python/Logs")
logs_directory.mkdir(parents=True, exist_ok=True)


def write():
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y_%m_%d %H-%M-%S")
    entry_filename = f"Entry {timestamp}.txt"
    entry_filepath = logs_directory / entry_filename

    entry_content = input("Write what is on your mind: ")
    with open(entry_filepath, "w") as entry_file:
        entry_file.write(entry_content)
    
    print(f"Journal entry with file name [{entry_filename}] created successfully")  


if __name__ == "__main__":
    write()
