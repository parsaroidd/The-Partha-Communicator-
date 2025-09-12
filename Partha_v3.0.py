import tkinter as parsaroidd
from Hex import password_save, password_read
import os, random  
import json as magical_file 
from datetime import datetime 

DataBase = {
    "ParsaRoidd":"Follow me on github"
}


file = os.path.expanduser("~")
path = os.path.join(file, "Downloads", "ParsaRoidd.json")


SQL = {}
SQL2 = {}

def sign_pop():

    global PassWord, User_name,result, veri, pop_up

    pop_up = parsaroidd.Tk()
    pop_up.title("Making an account here? RUN!!!")
    pop_up.geometry("500x400")

    parsaroidd.Label(pop_up, text="Create a cool name: (there isn't any cooler name that @ParsaRoidd on git hub)").pack()
    User_name = parsaroidd.Entry(pop_up)
    User_name.pack()

    parsaroidd.Label(pop_up, text="select sumn STRONG:(press submit after the 3rd box)").pack()
    PassWord = parsaroidd.Entry(pop_up)
    PassWord.pack()

    parsaroidd.Label(pop_up, text="wait wait gotta verify U").pack()
    veri = parsaroidd.Entry(pop_up)
    veri.pack()

    submit = parsaroidd.Button(pop_up, text="let's roll!", command= sign_up)
    submit.pack(pady=20)

    result = parsaroidd.Label(pop_up, text='')
    result.pack()
    pop_up.mainloop()

def sign_up():

    global user_name 

    user_name = User_name.get()
    passworD = PassWord.get()

    if user_name in DataBase:
        warn = f"i don't like {user_name} pick another one"
        result.config(text=warn)
    else:
        if 32 > len(passworD) > 5:
            verification = f"{user_name} type {password_save(password=passworD)} exactly as it is"
            
            password_save(password=passworD)
            result.config(text=verification)
            
            verif = veri.get()

            if len(passworD) != len(verif):
                
                warnn = f"don't fool me {user_name}... \n type {password_save(passworD)} exactly as it is"
                result.config(text=warnn)
            else:
                yay = f'we did itttt {user_name}!!!'
                result.config(text=yay)
                DataBase[user_name] = verif 
                with open(path, "w") as f:
                    magical_file.dump(DataBase, f, indent=4)
                code = input("Tell me your metadata: ")
                FILE = input("Give me ur json file name. (without .json): ")
                Decrypt(code, FILE)
                pop_up.destroy()


#gotta close the window in the right place...

                
        else:
            warning = f"this password isn't right"
            result.config(text=warning)

def Encrypt(message):

    global final 

    digit0= random.randint(1,9)
    digit1 = random.randint(1,9)
    digit2 = random.randint(1,9)
    digit3 = random.randint(1,9)
    literal = []
    timestamp = datetime.now() 
    keyy = f"{digit1}{digit0}{digit2}{digit3} // {timestamp}"

    if digit0 > 5:
        reverse = ''.join(reversed(message))
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
    SQL[keyy] = final 
    magic_file = os.path.join(file, "Downloads", f"{user_name}.json")
    with open(magic_file, "w") as f:
        magical_file.dump(SQL, f, indent=4)

def Decrypt():

    Code = code.get()
    file = FILE.get() 
  
    literal = []

    inside = os.path.join(file, "Downloads", f"{FILE}.json")
    try:
        if os.path.exists(inside):
            with open (inside, "r") as f:
                SQL2 = magical_file.load(f)

                try:
                    text = SQL2[Code]
                    if int(Code[1:2]) > 5:
                        reverse = ''.join(reversed(text))
                        shift = int(Code[2:3])
                    else:
                        reverse = text 
                        shift = int(Code[3:4])

                    for cgar in reverse:
                        if ord(cgar) >=75:
                            kalk = int(c=Code[0:1])
                        else:
                            kalk = shift 

                        
                        okokok = (ord(cgar) - kalk) 
                        literal.append(chr(okokok))

                    final = ''.join(literal)
                    SQL2[Code] = final 
                    print(SQL2)

                    
                except Exception:
                    print("code is not right")


        else:
            print("this file directory doesn't exit!")
    except Exception:

        print("try again")

def login():

    with open(path, "r") as f:
        DataBase = magical_file.load(f) 

    nam = name.get()
    pas = password.get()

    try:
        if password_read(DataBase[nam]) == pas: 

            alert = 'ur name is not cool i wanna still call you waltz. Welcome back waltz...'
            resultt.config(text=alert)
        
            pup_up.destroy()

            code = input("Tell me your metadata: ")
            FILE = input("Give me ur json file name. (without .json)")
            Decrypt(code, FILE)
    except KeyError:

        alertt = f"{nam} doesn't exist brah wanna sign up? if yes, write sign in name box..."
        resultt.config(text=alertt)
        if "sign" in nam:
            pup_up.destroy()
            sign_pop()

    else:
        pass
    
def login_pop():

    global name, password, pup_up, resultt 

    pup_up = parsaroidd.Tk()
    pup_up.title("Welcome backkkkkk waltzz")

    pup_up.geometry("500x300")

    parsaroidd.Label(pup_up, text="what was ur name waltz?").pack()
    name = parsaroidd.Entry(pup_up)
    name.pack(pady = 10)

    parsaroidd.Label(pup_up, text="wat was ur password?: ").pack()
    password = parsaroidd.Entry(pup_up)
    password.pack(pady=10)

    submit = parsaroidd.Button(pup_up, text="let's get in this hoe waltz.", command=login)
    submit.pack(pady=20)

    resultt = parsaroidd.Label(pup_up, text='')
    resultt.pack()

    pup_up.mainloop()

def UI():

    global code, FILE 

    WIN = parsaroidd.Tk()
    WIN.title("I am watching you, little boi~")
    WIN.geometry("600x600")

    parsaroidd.Label(WIN, text="give me the code: ").pack()
    code = parsaroidd.Entry(WIN)
    code.pack(pady=10)

    parsaroidd.Label(WIN, text="What is your .json file name waltz?").pack()
    FILE = parsaroidd.Entry(WIN)
    FILE.pack(pady=10)

    submit = parsaroidd.Button(WIN, text="let's decrypt it!", command=Decrypt)
    submit.pack(pady=20)

    show = parsaroidd.Label(WIN, text='')
    show.pack()

    WIN.mainloop()

UI()

    



