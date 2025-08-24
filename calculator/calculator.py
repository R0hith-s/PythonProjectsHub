import customtkinter as ctk

app=ctk.CTk()
app.geometry("470x570")
app.title("Calculator")

tabview = ctk.CTkTabview(app, width=450, height=420)
tabview.grid(row=1, column=0, padx=10, pady=10, columnspan=4)

calc_tab = tabview.add("Calculator")
history_tab = tabview.add("History")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

label=ctk.CTkLabel(calc_tab,text="",width=415,height=40,fg_color=("white","gray20"),text_color=("black","white"),font=("Consolas",20,"bold"),corner_radius=10)
label.grid(row=0,column=0,padx=10,pady=40,columnspan=4)

textbox=ctk.CTkTextbox(history_tab,width=440,height=380,state="disabled")
textbox.grid(pady=10)

def clear_history():
    textbox.configure(state="normal")
    textbox.delete("1.0","end")
    textbox.configure(state="disabled")

def clear_last():
    s=str(label.cget("text"))
    if s in ("","Error"):
        label.configure(text="")
    else:
        label.configure(text=s[:-1])

def click(value):
    s = str(label.cget("text"))
    if value in "+-*/":
        if not s or s[-1] in "+-*/":
            return
    label.configure(text=s + value)

def calculate():
    try:
        a = label.cget("text").strip()
        if not a:
            return
        while a and a[-1] in "+-*/":
            a = a[:-1]
        if a and a[0] in "*/":
            a = a[1:]
        if not a:
            return
        if a.isdigit():
            label.configure(text=a)
            textbox.configure(state="normal")
            textbox.insert("end", f"{a} = {a}\n")
            textbox.configure(state="disabled")
            textbox.see("end")
            return
        result = eval(a)
        label.configure(text=result)

        textbox.configure(state="normal")
        textbox.insert("end", f"{a} = {result}\n")
        textbox.configure(state="disabled")
        textbox.see("end")
    except:
        label.configure(text="Error", text_color="red")
        app.after(1500, lambda: label.configure(text="", text_color=("black","white")))


def clear():
    label.configure(text="")

def dark_mode():
    if switch.get()==1:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

switch=ctk.CTkSwitch(app,text="Dark Mode",command=dark_mode)
switch.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)



buttons=[
    ["7","8","9","+"],
    ["4","5","6","-"],
    ["3","2","1","*"],
    ["0","C","=","/"],
    ["<-"]
]
for r,row in enumerate(buttons,start=1):
    for c,value in enumerate(row):
        if value =="=":
            cmd=calculate
        elif value=="C":
            cmd=clear
        elif value =="<-":
            cmd=clear_last
        else:
            cmd=lambda val=value:click(val)
    
        btn=ctk.CTkButton(calc_tab,text=str(value),command=cmd,width=70,height=70,corner_radius=15)
        btn.grid(row=r,column=c,padx=5, pady=5)


clear_history_btn=ctk.CTkButton(history_tab,text="Clear History",command=clear_history,width=70,height=70,corner_radius=15)
clear_history_btn.grid(padx=15,pady=15)
if ctk.get_appearance_mode() =="Dark":
    switch.select()
else:
    switch.deselect()
app.mainloop()