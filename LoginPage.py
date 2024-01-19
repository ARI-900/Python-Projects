from tkinter import *
import tkinter.font as font
def call():
    act_pass = 'arj1234'
    act_name = 'Arijit Chowdhury'
    che_name =  name.get()
    che_pasw = pasw.get()

    if(act_name == che_name and act_pass == che_pasw):
        res_lbl['text']=f"Login Successfull"
        res_lbl['fg'] = f'green'
    else:
        res_lbl['text'] = f"Login Unsuccessfull"
        res_lbl['fg'] = f'red'


if __name__ == '__main__':
    root = Tk()
    root.geometry("350x250")
    root.maxsize(350,250)
    root.minsize(350,250)
    root.title("Login Form")
    root.configure(bg='#333333')

    lb1 = Label(root,text="Login",bg='#333333',fg='pink',font=('Arial BLack',12,'bold'))
    lb1.pack()
    name = StringVar()
    name_lb2 = Label(root,text="Username ",font=('Arial BLack',10,'bold'))
    pasw = StringVar()
    name_entry = Entry(root, font=('Arial BLack', 10, 'bold'),fg='navy',textvariable=name)
    pass_lb2 = Label(root, text="Password ", font=('Arial BLack', 10, 'bold'))
    pass_entry = Entry(root, font=('Arial BLack', 10, 'bold'), fg='navy',show='*',textvariable=pasw)
    btn1 = Button(root,text='Login',command=call)

    name_lb2.place(x=40,y=80)
    name_entry.place(x=140,y=80)
    pass_entry.place(x=140,y=120)
    pass_lb2.place(x=40,y=120)
    btn1.place(x=150,y=180)

    res_lbl = Label(root,text='',bg="#333333",font=('Arial BLack', 8, 'bold'))
    res_lbl.place(x=115,y=210)

    root.mainloop()
