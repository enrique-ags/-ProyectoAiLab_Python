from tkinter import *
from tkinter import messagebox
from juego import Juego
from PIL import ImageTk, Image


def login():
    userNameE = userNameEntry.get()
    passwordE = passwordEntry.get()
    p = Juego()
    if validate():
        flag = p.validate(userNameE,passwordE)
        if flag:
            clear()
            game_mode()
            
        else:
            MsgBox = messagebox.askquestion ('User Management','User does not exist, create it?',icon = 'info')
            if MsgBox == 'yes':
                open_win()

 
          


def clear():
    userNameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    

def validate():
    if len(userNameEntry.get())==0 or len(passwordEntry.get())==0:
        messagebox.showerror('Missing userName or password','Missing user name/password, please review') 
        return False   
    else:
        return True

def open_win():
   global username_var
   global password_var
   global password_confirmation_var
   global username_entry
   global passwordd_entry
   global passwordd_entry_confirmation
   global new

   username_var = StringVar()
   password_var = StringVar()
   password_confirmation_var = StringVar()

   new= Toplevel(root1)
   new.geometry("750x250")
   new.title("Create new user")
   lbl1 = Label(new,text='UserName: ')
   lbl1.place(x=10,y=25)
   lbl2 = Label(new,text='Password: ')
   lbl2.place(x=10,y=50)
   lbl3 = Label(new,text='Confirm Password: ')
   lbl3.place(x=10,y=80)
   username_entry = Entry(new,textvariable=username_var)
   username_entry.place(x=120, y = 25)

   passwordd_entry = Entry(new,show='*',textvariable=password_var)
   passwordd_entry.place(x=120, y = 50)
   passwordd_entry_confirmation = Entry(new, textvariable=password_confirmation_var, show='*')
   passwordd_entry_confirmation.place(x=120, y = 80)
   btnAccept = Button(new,text='Create', fg='blue',command=new_user)
   btnAccept.place(x=10,y=120)
   btnAccept = Button(new,text='Cancell', fg='blue',command=clear)
   btnAccept.place(x=80,y=120)

def new_user():
    if passwordd_entry.get() == password_confirmation_var.get(): 
        new_user_name = username_var.get()
        new_password = password_var.get()
        newid = Juego()
        print(new_user_name + '' + new_password)
        if newid.isDuplicated(new_user_name):
            messagebox.showerror('Error','User already exist')
        else:
            r=newid.insertNewUser(new_user_name,new_password,'1')
            if r:
                messagebox.showinfo('Success',message='User created succesfully')
                new.destroy()
            else:
                messagebox.showerror('Fail',message='an error happened')
                new.destroy()
    else:
        messagebox.showerror('Error','Password mismatch')



    

def game_mode():
   gm= Toplevel(root1)
   gm.geometry("750x250")
   gm.title("Gamer Mode") 

   btn01 = Button(gm,text='Training Mode',fg='blue', command=catalog_demon)  
   btn01.place(x=10,y=25) 
   btn02 = Button(gm,text='History Mode',fg='blue')   
   btn02.place(x=100,y=25) 

def catalog_demon():
    exec(open("demon.py").read())










   

def destroy_parent():
    root1.destroy()



   

root1 = Tk()
root1.geometry("800x600")
root1.title("Gamer zone")

lbl1 = Label(root1,text='UserName: ')
lbl1.place(x=10,y=25)

lbl2 = Label(root1,text='Password: ')
lbl2.place(x=10,y=50)


userNameEntry = Entry(root1)
userNameEntry.place(x=120, y = 25)

passwordEntry = Entry(root1,show='*')
passwordEntry.place(x=120, y = 50)


btnAccept = Button(root1,text='Login', fg='blue', command=login)
btnAccept.place(x=10,y=120)

btnAccept = Button(root1,text='Cancell', fg='blue',command=destroy_parent)
btnAccept.place(x=80,y=120)
root1.mainloop()







