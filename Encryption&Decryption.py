# Hello Bro How Are You!! I am not Done Yet , Dont Be woory about me...
from tkinter import *
import pybase64 as pyb
import tkinter.messagebox as tmess
password = 'arj1234'

# encrypt function ------------------------------------------
def encrypt():
    paswd2 = paswd.get()
    if (paswd2 == password):
        newwin = Toplevel(root)
        newwin.geometry('320x360')
        newwin.title('Encryted Code')
        newwin.resizable(0,0)
        newwin.config(background='#C39BD3')

        usermess = text1.get(1.0,END)
        # main logic
        encode_message = usermess.encode('ascii')
        base64_bytes = pyb.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")


    #     label
        Label(newwin,text='Code Is Encrypted',font=('Arial Black',9,'bold'),fg='black',bg='white').place(x=6,y=6)
    # text visit
        text2 = Text(newwin, font=('Arial Black', 10, 'bold'), fg='navy', bd=2,wrap=WORD)
        text2.place(x=5, y=45, height=100, width=310)
        text2.insert(END,encrypt)
    else:
        tmess.showwarning("Error Window","Please Eneter The Secret Code...")
# decrypt function ------------------------------------------
def decrypt():
    paswd2 = paswd.get()
    if (paswd2 == password):
        newwin2 = Toplevel(root)
        newwin2.geometry('320x360')
        newwin2.title('Encryted Code')
        newwin2.resizable(0,0)
        newwin2.config(background='#AED6F1')

        usermess = text1.get(1.0,END)

        # main logic
        encode_message = usermess.encode('ascii')
        base64_bytes = pyb.b64decode(encode_message)
        decrypt = base64_bytes.decode("ascii")

        # label
        Label(newwin2, text='Code Is Encrypted', font=('Arial Black', 9, 'bold'), fg='black', bg='white').place(x=6,
                                                                                                                y=6)
        # text visit
        text2 = Text(newwin2, font=('Arial Black', 10, 'bold'), fg='navy', bd=2, wrap=WORD)
        text2.place(x=5, y=45, height=100, width=310)
        text2.insert(END, decrypt)
    else:
        tmess.showwarning("Error Window","Please Eneter The Secret Code...")

def reset():
    text1.delete(1.0,END)
    paswd.set('')

if __name__ == '__main__':
    root = Tk()
    root.geometry('420x460')
    root.title('Encrytion and Decryption')
    root.config(background='#333333')
    root.maxsize(420,460)
    root.minsize(420,460)
    # label
    Label(root,text='Enter The Text for Encrytion and Decryption',font=('Arial Black',12,'bold'),fg='white',bg='#333333').place(x=10,y=5)
    #text visit
    text1 = Text(root,font=('Arial Black',19,'bold'),fg='navy',bd=2)
    text1.place(x=5,y=45,height=100,width=410 )
    # label secret
    Label(root,text="Enter Secret Key",font=('Arial Black',12,'bold'),fg='black',bg='#F4F6F6').place(x=135,y=160)
    # Entry visit
    paswd = StringVar()
    Entry(root,font=('Arial Black',10,'bold'),fg='navy',bg='white',show='*',textvariable=paswd,bd=2).place(x=120,y=200)

    # button
    Button(root,text="ENCRYPT",font=('Arial Black',11,'bold'),fg='white',bg='red',height=1,width=14,command=encrypt).place(x=50,y=250)
    Button(root, text="DECRYPT", font=('Arial Black', 11, 'bold'), fg='white', bg='green', height=1, width=14,command=decrypt).place(x=220,y=250)
    # Button Reset
    Button(root, text="RESET", font=('Arial Black', 11, 'bold'), fg='white', bg='blue', height=1, width=14,command=reset).place(x=130, y=310)
    root.mainloop()