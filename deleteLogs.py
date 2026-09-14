from writeLogs import targetDirectory
from pathlib import Path

def delete(): 
    readLocation = targetDirectory
    logsFiles = list(targetDirectory.glob("*.txt"))
    if not logsFiles:
        print("No files found")
        return
    else:
        logsFiles.sort(reverse=True)
    for index,logs in enumerate(logsFiles,start=1):
        print(f"[{index}] {logs}")

    try:
        choice = int(input("Enter the file number you want to Delete: "))
        
        if 1 <= choice <= len(logsFiles):
            selectedFile = logsFiles[choice-1]
            print(f"\n---- Content of {selectedFile} ----\n")
            with open(selectedFile,"r") as logsFiles:
                print(logsFiles.read())
            choice2=input("Are you sure you want to delete the file y/n ")
            if choice2.lower()=="y":
                selectedFile.unlink(missing_ok=True)
            elif choice2.lower()=="n":
                return
            else:
                print(" Invalid choice Try again later ") 

        else:
            print(" Invalid choice Try again later ")
    except ValueError:
        print("Invalid Input")
delete()