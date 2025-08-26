import customtkinter as ctk 
import random
app=ctk.CTk()
app.title("Number Guessing Game ")
app_width=850
app_height=900
sw=app.winfo_screenwidth()
sh=app.winfo_screenheight()
x=(sw-app_width)//2
y=(sh-app_height)//2
app.geometry(f"{app_width}x{app_height}+{x}+{y}")







ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def easy():
    l3.configure(text=f"Guess The Number \n Between 1 To 20")
    secret_number=random.randint(1,20)
def medium():
    l3.configure(text=f"Guess The Number \n Between 1 To 50")
    secret_number=random.randint(1,50)

def hard():
    l3.configure(text=f"Guess The Number \n Between 1 To 100")
    secret_number=random.randint(1,100)

def chk():
    pass

def reset():
    pass

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

btn1=ctk.CTkButton(f2,text="Easy",command=easy,height=50,width=190,font=("Segoe UI", 33,"bold"))
btn1.pack(pady=12)

btn2=ctk.CTkButton(f2,text="Medium",command=medium,height=50,width=190,font=("Segoe UI", 33,"bold"))
btn2.pack(pady=12)

btn3=ctk.CTkButton(f2,text="Hard",command=hard,height=50,width=190,font=("Segoe UI", 33,"bold"))
btn3.pack(pady=12)


f3=ctk.CTkFrame(app,height=230,width=900)
f3.pack(pady=10)

l3=ctk.CTkLabel(f3,text="",height=50,width=190,font=("Segoe UI", 42,"bold"))
l3.pack(pady=10)

cl=ctk.CTkLabel(f3,text="Chances Left : 5",height=50,width=190,font=("Segoe UI", 42,"bold"))
cl.pack(side="left")

l4=ctk.CTkLabel(f3,text="",height=50,width=600,font=("Segoe UI", 42,"bold"))
l4.pack()
f4=ctk.CTkFrame(app,height=300,width=900)
f4.pack(pady=5)

vcmd = (app.register(only_numbers), "%P")

entry=ctk.CTkEntry(f4,height=50,width=650,validate="key", validatecommand=vcmd,font=("Segoe UI", 32,"bold"))
entry.pack(pady=15)

cbtn=ctk.CTkButton(f4,text="Check",command=chk,height=50,width=190,font=("Segoe UI", 42,"bold"))
cbtn.pack(pady=10)

rbtn=ctk.CTkButton(f4,text="Reset",command=reset,height=50,width=190,font=("Segoe UI", 42,"bold"))
rbtn.pack(pady=10)

app.mainloop()