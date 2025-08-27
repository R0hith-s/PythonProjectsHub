import customtkinter as ctk 
import random
app=ctk.CTk()
app.title("Number Guessing Game ")
app_width=850
app_height=920
sw=app.winfo_screenwidth()
sh=app.winfo_screenheight()
x=(sw-app_width)//2
y=(sh-app_height)//2
app.geometry(f"{app_width}x{app_height}+{x}+{y}")
secret_number=0
diffculty=""
chances=5

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def disable_btn():
    btn1.configure(state="disabled")
    btn2.configure(state="disabled")
    btn3.configure(state="disabled")
def ensable_btn():
    btn1.configure(state="normal")
    btn2.configure(state="normal")
    btn3.configure(state="normal")

def easy():
    global secret_number,chances,diffculty
    chances = 5
    diffculty="easy"
    cl.configure(text="Chances Left : 5")
    l3.configure(text=f"Guess The Number \n Between 1 To 20")
    l4.configure(text="")
    secret_number=random.randint(1,20)
    disable_btn()
def medium():
    global secret_number,chances,diffculty
    chances = 5
    diffculty="medium"
    cl.configure(text="Chances Left : 5")
    l3.configure(text=f"Guess The Number \n Between 1 To 50")
    l4.configure(text="")
    secret_number=random.randint(1,50)
    disable_btn()
def hard():
    global secret_number,chances,diffculty
    chances = 5
    diffculty="hard"
    cl.configure(text="Chances Left : 5")
    l3.configure(text=f"Guess The Number \n Between 1 To 100")
    l4.configure(text="")
    secret_number=random.randint(1,100)
    disable_btn()
def chk():
    global chances,diffculty
    guess=entry.get()
    if diffculty=="":
        l3.configure(text="Select a diffculty first!")
        return

    if guess == "":
        l4.configure(text="Enter a number first!")
        return

    if chances == 0:
        l4.configure(text=f"❌You lost! Number was {secret_number}❌",text_color="red")
        entry.configure(state="disabled")
        cbtn.configure(state="disabled")
        return

    if int(secret_number) > int(guess):
        l4.configure(text="Enter a higher Number")
        chances-=1
        cl.configure(text="Chances Left : "+str(chances))
    elif int(secret_number) <int(guess):
        l4.configure(text="Enter a lower Number")
        chances-=1
        cl.configure(text="Chances Left : "+str(chances))
    if int(secret_number) == int(guess):
        l4.configure(text="👑 You won 👑",text_color="yellow")
        chances=0
        entry
        cbtn.configure(state="disabled")
    cl.configure(text="Chances Left : "+str(chances))

def reset():
    global chances,diffculty,secret_number
    chances=5
    cl.configure(text="Chances Left : 5")
    l3.configure(text="")
    l4.configure(text="")
    entry.delete(0,"end")
    entry.configure(state="normal")
    cbtn.configure(state="normal")
    ensable_btn()
    if diffculty =="easy":
        secret_number=random.randint(1,20)
        l3.configure(text=f"Guess The Number \n Between 1 To 20")
    if diffculty =="medium":
        secret_number=random.randint(1,50)
        l3.configure(text=f"Guess The Number \n Between 1 To 50")
    if diffculty =="hard":
        l3.configure(text=f"Guess The Number \n Between 1 To 100")
        secret_number=random.randint(1,100)


def only_numbers(text):
    return text.isdigit() or text == ""  

f1=ctk.CTkFrame(app,height=90,width=850,fg_color="transparent")
f1.pack(pady=10)

l1=ctk.CTkLabel(f1,text="Number Guessing Game 🎮",font=("Segoe UI", 42, "bold"))
l1.pack(pady=10)

f2=ctk.CTkFrame(app,height=200,width=650,fg_color="transparent")
f2.pack()

l2=ctk.CTkLabel(f2,text="Choose diffculty 👇",font=("Segoe UI", 42, "bold"))
l2.pack(pady=10)

btn1=ctk.CTkButton(f2,text="Easy",command=easy,height=50,width=190,font=("Segoe UI", 33,"bold"),fg_color="green",text_color="black")
btn1.pack(pady=12)

btn2=ctk.CTkButton(f2,text="Medium",command=medium,height=50,width=190,font=("Segoe UI", 33,"bold"),fg_color="yellow",text_color="black")
btn2.pack(pady=12)

btn3=ctk.CTkButton(f2,text="Hard",command=hard,height=50,width=190,font=("Segoe UI", 33,"bold"),fg_color="red",text_color="black")
btn3.pack(pady=12)


f3=ctk.CTkFrame(app,height=230,width=900)
f3.pack(pady=10,fill="x")

l3=ctk.CTkLabel(f3,text="",height=50,width=190,font=("Segoe UI", 42,"bold"))
l3.pack(pady=10)

cl=ctk.CTkLabel(f3,text="Chances Left : 5",height=50,width=100,font=("Segoe UI", 42,"bold"))
cl.pack(side="left")

f4=ctk.CTkFrame(app,height=300,width=900)
f4.pack(pady=5)

l4=ctk.CTkLabel(f4,text="",height=50,width=600,font=("Segoe UI", 42,"bold"))
l4.pack()
vcmd = (app.register(only_numbers), "%P")

entry=ctk.CTkEntry(f4,height=50,width=650,validate="key", validatecommand=vcmd,font=("Segoe UI", 32,"bold"))
entry.pack(pady=15)

cbtn=ctk.CTkButton(f4,text="Check",command=chk,height=50,width=190,font=("Segoe UI", 42,"bold"),fg_color="#90EE90",text_color="black")
cbtn.pack(pady=10)

rbtn=ctk.CTkButton(f4,text="Reset",command=reset,height=50,width=190,font=("Segoe UI", 42,"bold"),fg_color="red",text_color="black")
rbtn.pack(pady=10)

app.mainloop()