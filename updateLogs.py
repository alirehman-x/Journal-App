from writeLogs import targetDirectory
from pathlib import Path

def update(): 
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
        choice = int(input("Enter the file number you want to open: "))
        
        if 1 <= choice <= len(logsFiles):
            selectedFile = logsFiles[choice-1]
            print(f"\n---- Content of {selectedFile} ----\n")
            with open(selectedFile,"r") as logsFiles:
                print(logsFiles.read())
            choice2=input("would you like to edit the file y/n ")
            if choice2=="y":
                updatedData=input("Enter the text you want to append: ")
                with open(selectedFile,"a") as logsFiles:
                    logsFiles.write(updatedData)
            elif choice2=="n":
                return
            else:
                print(" Invalid choice Try again later ") 

        else:
            print(" Invalid choice Try again later ")
    except ValueError:
        print("Invalid Input")
update()