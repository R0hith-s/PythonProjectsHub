import customtkinter as ctk

app = ctk.CTk()
app_width=850
app_height=800
sw=app.winfo_screenwidth()
sh=app.winfo_screenheight()
x=(sw-app_width)//2
y=(sh-app_height)//2
app.geometry(f"{app_width}x{app_height}+{x}+{y}")









app.title("To-Do List App")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def dark_mode():
    if switch.get() == 1:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

def mini_w():
    mini=ctk.CTkToplevel(app)
    mini_width=350
    mini_height=200
    mini.geometry(f"{mini_width}x{mini_height}+{x}+{y}")
    mini.title("Add New Task")
    mini.lift() 
    mini.focus()
    mini.grab_set() 

    def add_task():
        a=entry.get()
        if a =="":
            return
        else:
            chk=ctk.CTkCheckBox(frame,text=a,font=("Segoe UI", 15, "bold"))
            chk.pack(pady=20,padx=25,fill="x")

    def close():
        mini.destroy()


    entry=ctk.CTkEntry(mini,width=300,height=35)
    entry.pack(pady=10)
    tbtn=ctk.CTkButton(mini,text="Add New Task",command=add_task)
    tbtn.pack(pady=10)
    cbtn=ctk.CTkButton(mini,text="Close",command=close)
    cbtn.pack(pady=10)


switch = ctk.CTkSwitch(app, text="Dark Mode", command=dark_mode, progress_color="#4cd137")
switch.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)


label = ctk.CTkLabel(app, text="To-Do-List", font=("Segoe UI", 30, "bold"))
label.pack(pady=(50, 10))


frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack(pady=10, fill="both", expand=False)

btn=ctk.CTkButton(frame,text="Add New Task",command=mini_w,width=220,height=80, font=("Segoe UI", 30, "bold"))
btn.pack(pady=40)

current_mode = ctk.get_appearance_mode()
if current_mode == "Dark":
    switch.select()
else:
    switch.deselect()

app.mainloop()
