from daterbase import *
def new_person():
    asking2 = input("Enter first name:  ")
    asking1 = input("Enter second name:  ")
    asking3 = input("Enter your age: ")
    c.execute('INSERT INTO new_user(fName, sName) VALUES(?, ?,?)',(asking2, asking1,asking3))
    conn.commit()
    repeat = input("Do you want to add another resident? Yes(Y) or No(N): ")
    if repeat == "Y" or repeat == "y":
        new_person()
    elif repeat == "N" or repeat == "n":
        print("Good Bye.")
    else:
        print("You have inputed the wrong input")
new_person()
