from tkinter import *
from tkinter import messagebox
import mysql.connector
# import tkinter as tk

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

global trial_no
trial_no=0

def trial():
    global trial_no
    trial_no+=1
    if trial_no==3:
        messagebox.showwarning("Warning","You have reached the limit!!")
        login_window.destroy()

def loginuser():
    username=user.get()
    password=code.get()
    if (username=="" or user =="UserID") or (password=="" or password=="Password"):
        messagebox.showerror("Entry Error!","Type User name or Password")
    else:
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',password='0328',database="studentregistration")
            mycursor=mydb.cursor()
            print("Connected to Database!!")
        except:
            messagebox.showerror("Connection error","Database connection not established")
            return
        command="use studentregistration"
        mycursor.execute(command)
        command="select * from login where Username=%s and Password=%s"
        mycursor.execute(command,(username,password))
        myresult=mycursor.fetchone()
        print(myresult)
        
        if myresult==None:
            messagebox.showinfo("Invalid","Invlid UserID or Password!!")
            trial()
        else:
            messagebox.showinfo("Login","Welcome Login successfull!!")
            login_window.destroy()
            import main

def register():
    login_window.destroy()
    import admin
        
        
login_window = Tk()
login_window.title("Login")
login_window.geometry("1250x700+210+100")
login_window.config(bg=background)
login_window.resizable(False,False)
def user_enter(e):
    user.delete(0,'end')
def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'UserID')
def password_enter(e):
    code.delete(0,'end')
def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
#ICON image

image_icon=PhotoImage(file="Images1/icon.png")
login_window.iconphoto(False,image_icon)


# Frame

frame=Frame(login_window,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="Images1/LOGIN.png")
Label(frame,image=backgroundimage).pack()

# user entry

user = Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=("Arial",24,"bold"))
user.insert(0,'UserID')
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_leave)
user.place(x=500,y=315)
 # pass entry
code = Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=("Arial",24,"bold"))
code.insert(0,'Password')
code.bind("<FocusIn>",password_enter)
code.bind("<FocusOut>",password_leave)
code.place(x=500,y=410)

########################hide and show button


button_mode=True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye,activebackground="white")
        code.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=openeye,activebackground="white")
        code.config(show="")
        button_mode=True
        
        
openeye=PhotoImage(file="Images1/openeye.png")
closeeye=PhotoImage(file="Images1/close eye.png")
eyeButton=Button(frame,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=780,y=410)



loginButton=Button(login_window,text="LOGIN",bg="#1f5675",width=10,height=1,font=("Arial",16,"bold"),bd=0,command=loginuser)
loginButton.place(x=570,y=600)

label=Label(login_window,text="Don't have an account?",fg="#fff",bg="#00264d",font=("Microsoft YaHei UI Light",9))
label.place(x=500,y=500)

registerButton=Button(login_window,width=10,text="add new user",border=0,bg="#002643",cursor="hand2",fg="#57a1f8",command=register)
registerButton.place(x=650,y=500)
login_window.mainloop()
# # Global variable to track login attempts
# login_attempts = 0

# def login():
#     global login_attempts
#     # Validate username and password
#     username = username_entry.get()
#     password = password_entry.get()

#     # Connect to MySQL database
#     try:
#         connection = mysql.connector.connect(
#             host="your_host",
#             user="your_username",
#             password="your_password",
#             database="your_database"
#         )

#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
#         user = cursor.fetchone()

#         if user:
#             # Close current window
#             login_window.destroy()

#             # Open new window for image display
#             display_images_window()

#         else:
#             login_attempts += 1
#             if login_attempts >= 3:
#                 messagebox.showerror("Login Failed", "Maximum login attempts reached. Exiting...")
#                 login_window.destroy()
#             else:
#                 messagebox.showerror("Login Failed", "Invalid username or password")

#     except mysql.connector.Error as error:
#         messagebox.showerror("Database Error", f"Failed to connect to database: {error}")

# def display_images_window():
#     # Create a new window for image display
#     images_window = tk.Tk()
#     images_window.title("Image Display")
    
#     # Load and display images
#     # Example: image_label = tk.Label(images_window, image=your_photoimage)
#     #          image_label.pack()

#     # Add back button
#     back_button = tk.Button(images_window, text="Back", command=images_window.destroy)
#     back_button.pack()

#     images_window.mainloop()

# def admin_login():
#     admin_password = "your_admin_password"
#     if admin_password_entry.get() == admin_password:
#         # Close current window
#         login_window.destroy()

#         # Open admin panel window
#         admin_panel_window()

#     else:
#         messagebox.showerror("Admin Login Failed", "Incorrect admin password")

# def admin_panel_window():
#     admin_window = tk.Tk()
#     admin_window.title("Admin Panel")

#     # Add functionality to manage users (add/remove)

#     admin_window.mainloop()

# # Create login window


# # Add username and password entry fields
# username_label = tk.Label(login_window, text="Username:")
# username_label.grid(row=0, column=0)
# username_entry = tk.Entry(login_window)
# username_entry.grid(row=0, column=1)

# password_label = tk.Label(login_window, text="Password:")
# password_label.grid(row=1, column=0)
# password_entry = tk.Entry(login_window, show="*")
# password_entry.grid(row=1, column=1)

# # Add login button
# login_button = tk.Button(login_window, text="Login", command=login)
# login_button.grid(row=2, columnspan=2)

# # Add admin login section
# admin_password_label = tk.Label(login_window, text="Admin Password:")
# admin_password_label.grid(row=3, column=0)
# admin_password_entry = tk.Entry(login_window, show="*")
# admin_password_entry.grid(row=3, column=1)

# admin_login_button = tk.Button(login_window, text="Admin Login", command=admin_login)
# admin_login_button.grid(row=4, columnspan=2)

# login_window.mainloop()