usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "1234" :
    print("-------------------------------")
    print("    Welcome to NOTShop !!!!    ")
    print("-------------------------------")
    print("What would you like to have?")
    print("  Product           Price")
    print("1. Apple          : 10 THB")
    print("2. Banana         : 12 THB")
    print("3. Orange         : 8  THB")
    print("4. Coconut        : 18 THB")
    print("5. Mango          : 15 THB")
    applePrice = 10
    bananaPrice = 12
    orangePrice = 8
    coconutPrice = 18
    mangoPrice = 15
    userSelected = int(input(">"))
    if userSelected == 1 :
        print("How many apples do you want?")
        orderInput = int(input())
        print("The Total is :",applePrice*orderInput,"THB")
    elif userSelected == 2 :
        print("How many bananas do you want?")
        orderInput = int(input())
        print("The Total is :",bananaPrice*orderInput,"THB")
    elif userSelected == 3 :
        print("How many oranges do you want?")
        orderInput = int(input())
        print("The Total is :",orangePrice*orderInput,"THB")
    elif userSelected == 4 :
        print("How many coconuts do you want?")
        orderInput = int(input())
        print("The Total is :",coconutPrice*orderInput,"THB")
    elif userSelected == 5 :
        print("How many mangos do you want?")
        orderInput = int(input())
        print("The Total is :",mangoPrice*orderInput,"THB")
    print("-------------------------------")
    print("Thank you! for shopping with us")
    print("-------------------------------")
else:
    print("Wrong username or password!")