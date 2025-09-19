import tkinter as ParsaRoidd 
import os, random
import json as magical_file 
from datetime import datetime 

file = os.path.expanduser("~")
path = os.path.join(file, "Downloads", "ParsaRoidd.json")

SQL = {
    "test": "123"
} 


def user_inter_face():

    start = ParsaRoidd.Tk()
    start.title("Welcome Waltz")
    start.geometry("400x400")

    decrypt = ParsaRoidd.Button(start, text="i wanna decrypt sumn", command=Encrypt_ward)
    decrypt.pack(pady= 10)

    encrypt = ParsaRoidd.Button(start, text=" wanna encrypt?: ", command=Decrypt)
    encrypt.pack(pady=10)

    start.mainloop()


def Encrypt_ward():

    global Message, ward 

    ward = ParsaRoidd.Tk()
    ward.title("ur message Encryption:  ")
    ward.geometry("400x400")

    ParsaRoidd.Label(ward, text="What you want to encrypt waltz? ").pack(pady=10)
    Message = ParsaRoidd.Entry(ward)
    Message.pack(pady=10)

    submit = ParsaRoidd.Button(ward, bg="#0000ff", fg="#ffffff", text="lets Encrypt this hoe..", command= Encrypt)
    submit.pack()

    ward.mainloop() 


def Encrypt():

    global final

    message = Message.get()


    digit0= random.randint(1,9)
    digit1 = random.randint(1,9)
    digit2 = random.randint(1,9)
    digit3 = random.randint(1,9)
    literal = [] 
    timestamp = datetime.now() 
    keyy = f"{digit1}{digit0}{digit2}{digit3} // {timestamp}"

    if digit0 > 5:
        reverse = ''.join(reversed(str(message)))
        shift = digit2
    else:
        reverse = message 
        shift = digit3 

    for charac in reverse:
        if ord(charac) >= 75:
            kalk = digit1
        else:
            kalk = shift 
    
        okokok = (ord(charac) + kalk) % 0X110000  #unicode overflow i learned from somewhere gotta study more about it 
        literal.append(chr(okokok))

    
    final = ''.join(literal)
    ParsaRoidd.Label(ward, text=f"{final}").pack()

    SQL[keyy] = final 
    magic_file = os.path.join(file, "Downloads", f"{user_name}.json")
    
    with open(magic_file, "w") as f:
        magical_file.dump(SQL, f, indent=4)

def Decrypt_itself():

    global just 

    message = SQL[parth]

    digit0= int(parth[1])
    digit1 = int(parth[0])
    digit2 = int(parth[2])
    digit3 = int(parth[3])
    literal = [] 

    if digit0 > 5:
        reverse = ''.join(reversed(str(message)))
        shift = digit2
    else:
        reverse = message 
        shift = digit3 

    for charac in reverse:
        if ord(charac) >= 75:
            kalk = digit1
        else:
            kalk = shift
        okokok = (ord(charac) - kalk) % 0X110000 
        literal.append(chr(okokok))

    
    just = ''.join(literal)
    ParsaRoidd.Label(panel, text=f"{just}").pack()


def Decrypt(): 

    global parth, panel 

    panel = ParsaRoidd.Tk()
    panel.title("let's encrypt ur crap")
    panel.geometry("400x400")

    ParsaRoidd.Label(panel, text="What was ur parth code ?: ")
    parth = ParsaRoidd.Entry(panel)
    parth.pack(pady=10)

    submit = ParsaRoidd.Button(panel, text="press me to start translating", command=Decrypt_itself)
    submit.pack(pady=10)

    ParsaRoidd.Label(panel, text=f"{just}").pack()
    panel.mainloop()




def login_itself():

    with open(path, "r") as f:
        SQL = magical_file.load(f)
    
    name = user_name.get()
    key = password.get()
    

    try:
        if SQL[name] == key:

            ParsaRoidd.Label(main_UI, text="I'm gonna still call u waltz idc...").pack(pady=10)
            main_UI.destroy()
            user_inter_face()

    except Exception:
        ParsaRoidd.Label(main_UI, text="sumn is wrong waltz..").pack(pady=10) 

def getting_login():

    global password, user_name  

    Login.config(state="disabled") 
    
    ParsaRoidd.Label(main_UI, text="What was ur name? U R not that importent for me to remember: ").pack()
    user_name = ParsaRoidd.Entry(main_UI)
    user_name.pack(pady=10)

    ParsaRoidd.Label(main_UI, text="What was ur passy?").pack()
    password = ParsaRoidd.Entry(main_UI)
    password.pack(pady=10)

    submit = ParsaRoidd.Button(main_UI, bg="#0000ff", fg="#ffffff", text="let's get in this hoe waltz", command=login_itself)
    submit.pack(pady=10)

def sign_in():
    
    value = User_Name.get()
    key = Password.get()

    if value not in SQL and len(key) > 5:

        SQL[value] = key

        with open(path, "w") as f:
            magical_file.dump(SQL, f, indent=4)
      
        ParsaRoidd.Label(main_UI, text="welcome aboard i guess.... ").pack(pady=10)
        main_UI.destroy()
        user_inter_face()

    else:
        ParsaRoidd.Label(main_UI, text="What is this shit? i don't like it pick some other stuff").pack(pady=10) 

def siginig_in():

    global Password, User_Name 

    sign_up.config(state="disabled") 
    
    ParsaRoidd.Label(main_UI, text="pick some name. ofc there is no better name that @ParsaRoidd on github! ").pack()
    User_Name = ParsaRoidd.Entry(main_UI)
    User_Name.pack(pady=10)

    ParsaRoidd.Label(main_UI, text="What was ur passy?").pack()
    Password = ParsaRoidd.Entry(main_UI)
    Password.pack(pady=10)

    submit = ParsaRoidd.Button(main_UI,  bg="#0000ff", fg="#ffffff", text="I wouldn't click this honestly...", command=sign_in)
    submit.pack(pady=10)

main_UI = ParsaRoidd.Tk()
main_UI.title("Want to get in here! RUN!!!!")
main_UI.geometry("500x1000")


sign_up = ParsaRoidd.Button(main_UI, bg="#0000ff", fg="#ffffff", text="don't have an account? create one!", command=siginig_in)
sign_up.pack(pady=40)

Login = ParsaRoidd.Button(main_UI, bg="#0000ff", fg="#ffffff", text="have an account waltz? let's get in this hoe then...", command=getting_login)
Login.pack(pady=10)

main_UI.mainloop()