print("Hello !")
print("This is my new feature code")

def Zelda():
    n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? (l/r)")
    i = 0
    while n == "right" or n == "Right" or n == 'r' or n == 'R':
        i += 1
        if i < 3:
            face = ':)'
        else:
            face = ':|'
        n = input("You are in the Lost Forest\n****************\n****************\n "+face+"\n****************\n****************\nGo left or right? (l/r)")
    print("\nYou got out of the Lost Forest!\n\o/")
