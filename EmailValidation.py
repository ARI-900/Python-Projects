'''
arjchowdhury900@gmail.com
a - z , 0 - 9 ,
. , _ one times
@ onr times
. -3 and -4 position
'''
from tkinter import *
import re
def emailCheck():

    userEmail = email.get()
    email_condition = "^[a-z]+[\_.]?+[a-z]+[0-9]+[@]\w+[.]\w{2,3}$"

    x = re.search(email_condition,userEmail)
    if x:
        str = 'Right Email'
        T1.insert(END,str)
        T1.config(fg='green')
    else:
        str = 'Wrong Email'
        T1.insert(END, str)
        T1.config(fg='red')

def reset():
    email.set('')
    T1.delete(1.0,END)

if __name__ == '__main__':
    root = Tk()
    root.geometry('320x380')
    root.title("Email Validation Checker")
    root.resizable(0,0)
    root.config(background='#333333')

    # heading
    Label(root,text='Enter Your Email Here ',font=('Arial Black',14,"bold"),fg='White',bg='#333333').pack()
    # Entry box
    email = StringVar()
    Entry(root,font=('Arial Black',12,"bold"),fg='navy',bd=2,textvariable=email).place(height=30,width=300,x=10,y=40)
    #Button
    Button(root,text='ENTER',font=('Arial Black',10,"bold"),fg='black',bg='white',bd=2,height=1,width=7,command=emailCheck).place(x=50,y=90)

    # result Text
    T1 = Text(root,bd=2,font=('Arial Black',12,"bold"),fg='navy')
    T1.place(x=40,y=160,height=30,width=240)

    # Reset Button
    Button(root, text='RESET', font=('Arial Black', 10,"bold"),fg='black',bg='white',bd=2,height=1,width=7,command=reset).place(x=200, y=90)
    root.mainloop()