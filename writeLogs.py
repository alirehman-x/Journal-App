from datetime import datetime;
from pathlib import Path


targetDirectory= Path("D:/Docs/Code/Python/Logs")
targetDirectory.mkdir(parents = True, exist_ok = True)
def write():
   

    now = datetime.now()
    timeStamp= now.strftime("%Y_%m_%d %H-%M-%S")
    filename =f"Entry {timeStamp}.txt"
    filePath = targetDirectory / filename

    entry = input("Write what is on your mind: ")
    with open(filePath,"w") as file:
        file.write(entry)
    
    print(f"Journal entry with file name [{filename}] created successfully")  


if __name__ == "__main__":
    write()
    