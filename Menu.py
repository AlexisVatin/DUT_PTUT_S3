from Test.Test1 import Testbot

def menu() :
    print("1. Lancer le bot")
    print("2. Modifier liste")
    print("3. Quit")
    selection=int(input("Enter choice : "))
    if selection == 1:
        Testbot()
        #good ()
        print("Lancement du bot")
        #if Test1 == true:
           #selection2=str(input("Enter anything to return to menu"))
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



# try catch

# try:
#     selection == 1
#     good() # le bot est lancé
#     if str(input("Appuyez sur une touche pour arreter le bot"))
#         break
#
# try:
#     selection == 2
#     print("bad")
# try:
#     selection == 3
#     print("A bientot")
# except ValueError:
#     print("Oops!  That was no valid number.  Try again...")
#     menu()
#          # if Test1 == true:
#          #    selection2=str(input("Enter anything to return to menu"))
#          #    menu()
