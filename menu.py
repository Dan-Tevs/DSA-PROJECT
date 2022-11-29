def menu():
    print("<><><><><><><>")
    print("| [1] Menu   |")
    print("| [2] About  |")
    print("| [3] Exit   |")
    print("<><><><><><><>")

def option1():
    print("Select a game")
    from gameMenu import game_menu
    game_menu()
    

def option2():
    print("About game")
    print("This game is our Project. Our goal is to implementing Stack, Queue, and Linked Liist game.")
    menu()

def option3():
    print("Program terminated!")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    else:
        print("Invalid option!")
    break
