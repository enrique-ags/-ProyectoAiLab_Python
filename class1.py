from email import message
from tkinter import *
from tkinter import messagebox




from juego import Juego

def login():
    if validate():
        p1 = Juego()
        userid = userName.get()
        if p1.isDuplicated(userid):
            messagebox.showerror("Duplicated user","user Exists")
        else:
            MsgBox = messagebox.askquestion('User Management','User does not exist, create it?',icon = 'info')
            print(MsgBox)







def clear():
    userName.delete(0,END)
    password.delete(0,END)
    confirmPass.delete(0,END)

def validate():
    if len(userName.get())==0 or len(password.get())==0 or len(confirmPass.get())==0:
        messagebox.showerror('Missing userName or password','Missing user name/password, please review')
    elif(password.get()!= confirmPass.get()):
        messagebox.showerror('Password is not matching','Password is not matching')
    else:
        return True

    




root = Tk()
root.geometry("800x600")

lbl1 = Label(root,text='UserName: ')
lbl1.place(x=10,y=25)

lbl2 = Label(root,text='Password: ')
lbl2.place(x=10,y=50)

lbl3 = Label(root,text='Confirm Password: ')
lbl3.place(x=10,y=80)
userName = Entry(root)
userName.place(x=120, y = 25)

password = Entry(root)
password.place(x=120, y = 50)

confirmPass = Entry(root)
confirmPass.place(x=120, y = 80)


btnAccept = Button(root,text='Login', fg='blue',command=login)
btnAccept.place(x=10,y=120)

btnAccept = Button(root,text='Cancell', fg='blue',command=clear)
btnAccept.place(x=80,y=120)













root.mainloop()
