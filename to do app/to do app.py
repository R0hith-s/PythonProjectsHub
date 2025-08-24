import customtkinter as ctk

app = ctk.CTk()
app_width=850
app_height=800
sw=app.winfo_screenwidth()
sh=app.winfo_screenheight()
x=(sw-app_width)//2
y=(sh-app_height)//2
app.geometry(f"{app_width}x{app_height}+{x}+{y}")
task=[]






app.title("To-Do List App")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def dark_mode():
    if switch.get() == 1:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

def add_task():
    mini=ctk.CTkToplevel(app)
    mini_width=350
    mini_height=200
    m_x=(sw - mini_width) // 2
    m_y=(sh - mini_height) // 2
    mini.geometry(f"{mini_width}x{mini_height}+{m_x}+{m_y}")
    mini.title("Add New Task")
    mini.lift() 
    mini.focus()
    mini.grab_set() 
    
    def edit():
        mini2=ctk.CTkToplevel(app)
        mini2_width=350
        mini2_height=200
        mini2.geometry(f"{mini2_width}x{mini2_height}+{m_x}+{m_y}")
        mini2.title("Add New Task")
        mini2.lift() 
        mini2.focus()
        mini2.grab_set() 

        edit_entry=ctk.CTkEntry(mini2,height=35,width=300)
        edit_entry.place(relx=0.5, rely=0.15, anchor="center")

    def remove(a):
        a.destroy()
        task.remove(a)
        
    def submit():
        a=entry.get()
        if a =="":
            return
        else:
            frame_row=ctk.CTkFrame(frame)
            frame_row.pack(pady=5,padx=5, fill="x")
            chk=ctk.CTkCheckBox(frame_row,text=a,font=("Segoe UI", 15, "bold"))
            chk.pack( padx=5, pady=5,side="left")
            rbtn=ctk.CTkButton(frame_row,text="Remove",command=lambda: remove(frame_row))
            rbtn.pack(padx=5, pady=5,side="right")
            ebtn=ctk.CTkButton(frame_row,text="Edit",command=edit)
            ebtn.pack(padx=5, pady=5,side="right")
            task.append(frame_row)
            
        mini.destroy()




    entry=ctk.CTkEntry(mini,width=300,height=35)
    entry.pack(pady=10)
    tbtn=ctk.CTkButton(mini,text="Add New Task",command=submit)
    tbtn.pack(pady=10)



switch = ctk.CTkSwitch(app, text="Dark Mode", command=dark_mode, progress_color="#4cd137")
switch.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)


label = ctk.CTkLabel(app, text="To-Do-List", fg_color="transparent", font=("Segoe UI", 30, "bold"))
label.pack(pady=(50, 10))


frame = ctk.CTkScrollableFrame(app,width=400, height=900)
frame.pack(pady=10, fill="both", expand=False)

btn=ctk.CTkButton(frame,text="Add New Task",command=add_task,width=220,height=80, font=("Segoe UI", 30, "bold"))
btn.pack(pady=40)

current_mode = ctk.get_appearance_mode()
if current_mode == "Dark":
    switch.select()
else:
    switch.deselect()

app.mainloop()
