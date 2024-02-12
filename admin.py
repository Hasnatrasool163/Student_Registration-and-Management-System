from tkinter import *
from tkinter import messagebox
import mysql.connector

background="#06283D"
framebg="#EDEDED"
framefg="#06283d"

root=Tk()
root.title("New User Registration")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False,False)


def register():
    username = user.get()
    password = code.get()
    admincode=adminaccess.get()
    
    print(username,password,admincode) # checking to confirm once 
    if admincode=="032842":
        if (username=="" or user =="UserID") or (password=="" or password=="Password"):
            messagebox.showerror("Entry Error!","Type User name or Password")
        else:
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',password='0328')
                mycursor=mydb.cursor()
                print("Connection Established!!")
            except:
                messagebox.showerror("Connection error","Database Connection not established!")
                
            try:
                command="create database StudentRegistration"
                mycursor.execute(command)
                
                command="use  StudentRegistration"
                mycursor.execute(command)
                
                command="create table login (user int auto_increment key not null,username varchar(100),password varchar(100));"
                mycursor.execute(command)
                
                
                
            except:
                mycursor.execute("use  StudentRegistration")
                mydb=mysql.connector.connect(host='localhost',user='root',password='0328',database="StudentRegistration")
                mycursor=mydb.cursor()
                
                command="insert into login(username,password) values(%s,%s)"
                mycursor.execute(command,(username,password))
                mydb.commit()
                messagebox.showinfo("Admin","New User added Successfully!!")
    else:
        messagebox.showerror("Admin code ","Input Correct Admin code to add new user")
def login():
    root.destroy()
    import login



def user_enter(e):
    user.delete(0,'end')
def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,"UserID")
        
def password_enter(e):
    code.delete(0,'end')
def password_leave(e):
    if code.get()=='':
        code.insert(0,"Password")
#icon

image_icon=PhotoImage(file="Images1/icon.png")
root.iconphoto(False,image_icon)
# root.iconname("ADMIN")


# background#######################################################################

frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="Images1/register.png")
Label(frame,image=backgroundimage).pack()


adminaccess=Entry(frame,width=15,fg="#000",border=0,bg="#e8ecf7",font=("Arial",20,"bold"),show="*")
adminaccess.focus()
adminaccess.place(x=550,y=280)

# user entry############################################################
user=Entry(root,width=10,fg="#fff",bg="#375174",border=0,font=("Arial",20,"bold"))
user.insert(0,"UserID")
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_leave)
user.place(x=500,y=380)

# pass entry########################################
code=Entry(root,width=10,fg="#fff",bg="#375174",border=0,font=("Arial",20,"bold"))
code.insert(0,"Password")
code.bind("<FocusIn>",password_enter)
code.bind("<FocusOut>",password_leave)
code.place(x=500,y=470)

# button mode########################################
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
eyeButton.place(x=780,y=470)
##########################################################3

regis_button=Button(root,text="ADD NEW USER",bg="#455c88",fg="white",width=13,height=1,font=("Arial",16,"bold"),bd=0,command=register)
regis_button.place(x=530,y=600)

backbuttonimage=PhotoImage(file="Images1/backbutton.png")
backbutton=Button(root,image=backbuttonimage,fg="#deeefb",command=login)
backbutton.place(x=20,y=15)


root.mainloop()