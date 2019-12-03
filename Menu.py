#from Test import Test1


def menu() :
    print("1. Lancer le bot")
    print("2. Modifier liste")
    print("3. Quit")
    selection=int(input("Enter choice : "))
    if selection == 1:
        #Test1
        good ()
        print("Lancement du bot")
        if Test1 == true:
            selection2=str(input("Enter anything to return to menu"))
            menu()
    elif selection == 2:
        bad()
        print("bad");
    elif selection == 3:
        exit()
    else:
        print("Invalid choice, Enter 1-3")
        menu()

def good () :
    print("Good")
    anykey=input("Enter anything to return to menu")
    menu()

def bad () :
    print ("Bad")
    anykey=input("Enter anything to return to menu")
    menu()

#main routin

menu()

