import random

option = input("Roll the dice? (y/n): ")

while option not in ("y", "n", "Y", "N"):
    print('Invalid input!')
    option = input("Roll the dice? (y/n): ")

if option == "y" or option == "Y":
    while True:
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(f"({x}, {y})")
        option = input("Roll the dice? (y/n): ")
        while option not in ("y", "n", "Y", "N"):
            print('Invalid input!')
            option = input("Roll the dice? (y/n): ")
        if option == 'n' or option == 'N':
            print("Thanks for playing!")
            break
elif option == 'n' or option == 'N':
    print("Thanks for playing!")