
from class_a import Die

die = Die()
def main():
    while True:
        print("1. Roll die")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            die.roll()
            print(die)
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid. Enter 1 or 2.")
main()