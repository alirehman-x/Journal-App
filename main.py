from write_logs import write
from read_logs import read
from update_logs import update
from delete_logs import delete
from search_logs import search


if __name__ == "__main__":
    print("\n---welcome to journaling app----\n")
    
    while True:
        print("what would you like to do? ")
        try:
            choice = int(input("Press 1 for write 2 for read 3 for update 4 for delete 5 for seach 6 for exit: "))
            if choice == 1:
                write()
            elif choice == 2:
                read()
            elif choice == 3:
                update()
            elif choice == 4:
                delete()
            elif choice == 5:
                search()
            elif choice == 6:
                print("Thank you for using Journal App. Goodbye!")
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, 4, 5 or 6.\n")
        except ValueError:
            print("Unsupported Input. Please enter a number.\n")
