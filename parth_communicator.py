#______________________________________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________________< this is created by @Parsaroidd on github >______________________________________________________________________
#_____________________________________________________________________<    this is unfinished, my first attempt   >______________________________________________________________________
#________________________________________________________________________________________________________________________________________________________________________________________ 




import tkinter as tk 
import random as r 
import json , os

file = os.path.expanduser("~")
path = os.path.join(file, "Documents", "User_data.json")


Database = {
    '':'123'
}

info = {}


import random as r 

r0 = r.randint(1,9)
r1 = r.randint(1,9)

def partha():

    global x2, key 
 
    stage_one = []
    stage_two = []




    key = f'{r0}{r1}'

    text = input("enter ur shit: ")

    for i in text:
        ii = chr(ord(i) + r0)
        stage_one.append(ii)
    x = ''.join(stage_one)


    for u in x:
        uu = chr(ord(u) + r1)
        stage_two.append(uu)
    x2 = ''.join(stage_two) 


def ahtrap():


    stage_one = []
    stage_two = []

    for i in x2:
        ii = chr(ord(i) - r0)
        stage_one.append(ii)
    x = ''.join(stage_one)


    for u in x:
        uu = chr(ord(u) - r1)
        stage_two.append(uu)
    x3 = ''.join(stage_two) 
    print(x3)

def sign_up():

    name = nname_entry.get()
    if name in Database:
        tax = f"{name} is perimium name, you can not pick it"
        ressult_label.config(text=tax)
    else:
        passw = ppassword.get()
        if passw != '':
            Database[name] = passw
            tax = f'welcome aboard dear {name}!'
            ressult_label.config(text=tax)
            ward_f.destroy()
    ward_f.mainloop()

ward_f = tk.Tk()
ward_f.title("The sign up page")
ward_f.geometry("400x400")

tk.Label(ward_f, text="Welcome! create a Cool name For urself").pack()
nname_entry = tk.Entry(ward_f)
nname_entry.pack()

tk.Label(ward_f, text="set up a strong password: ").pack()
ppassword = tk.Entry(ward_f)
ppassword.pack()

subb = tk.Button(ward_f, text="submit", command=sign_up)
subb.pack()

ressult_label = tk.Label(ward_f, text='')
ressult_label.pack()

    

def login():

    User_name = Name_entry.get()
    Password = PassWord.get()

    if Database[User_name] == Password:
        tex = f"Hello {User_name} ! Login was successful.."
    else:
        tex = "Incorrect password or Username.."
    
    result_label.config(text=tex) 
    partha()
    ahtrap()


def UI():
    sign_up()
    login()


UI()