import random
import csv



f = open("passwords.csv", "a+",newline = "\n")
w = csv.writer(f,delimiter = "|")


l_pwd = []

def alphabet_add():
    global l_pwd
    s_alphabet = "abcdefghijklmnopqrstuvwxyz"
    l_alphabet = list(s_alphabet)
    a = random.randint(0,25)
    l_pwd.append(l_alphabet[a])

def int_add():
    global l_pwd
    s_int = "0123456789"
    l_int = list(s_int)
    a = random.randint(0,9)
    l_pwd.append(l_int[a])
    
def spec_add():
    global l_pwd
    s_spec =  "!@#$%^&*()~-_"
    l_spec = list(s_spec)
    a = random.randint(0,11)
    l_pwd.append(l_spec[a])


while True:

    name = input("Enter name of Website/App: ")
    user = input("Enter Username/Email: ")
    x = int(input("Enter Number of Characters for Password: "))
    for i in range(x):
        a = random.randint(0,3)
        if a == 0:
            alphabet_add()
        if a == 1:
           int_add() 
        if a == 2:
            spec_add()

    c = input("Add more? Y/N ")
    if c.upper() == "Y":
        continue
    else:
        
        pwd = ""
        for i in l_pwd:
            pwd = pwd + str(i)
    
        rec = [name.upper(),user,pwd]
        w.writerow(rec)
        f.close()
        print("Succesfully Saved All Data")
        break


                 

