from tkinter import *
import tkinter.simpledialog as tksim
import os
import sys

def powerbtn(n):
    # restart
    if(n==1):
        os.system('shutdown /r /t 1')       # os.system('shutdown r/ t/ 1')

    # shutdown
    elif(n==2):
        os.system('shutdown /s /t 1')       # os.system('shutdown /s /t 1')

    # restart time
    elif(n==3):
        os.system('shutdown /r /t 20')          # os.system('shutdown /r /t 20')

    # logout
    elif(n==4):
        os.system('shutdown -1')                    # os.system('shutdown -1')


if __name__ == '__main__':
    root = Tk()
    root.geometry('320x350')
    root.resizable(0,0)
    root.title("Shutdown Window")
    root.config(background='#333333')

    # Heading
    Label(root,text='POWER BUTTON',font=('Arial Black',20,'bold'),fg='whitesmoke',bg='#333333').pack()
    # restart button
    r_button = Button(root,text='Restart',font=('Time New Roman',15,'bold'),height=1,relief=RAISED,cursor="plus",command=lambda :powerbtn(1))
    r_button.pack(pady=10)
    # shutdown button
    s_button = Button(root, text='Shutdown', font=('Time New Roman', 15, 'bold'), height=1, relief=RAISED, cursor="plus",command=lambda :powerbtn(2))
    s_button.pack(pady=10)
    # restart time button
    rt_button = Button(root, text='Restart Time', font=('Time New Roman', 15, 'bold'), height=1, relief=RAISED, cursor="plus",command=lambda :powerbtn(3))
    rt_button.pack(pady=10)
    # logout time button
    rt_button = Button(root, text='Logout', font=('Time New Roman', 15, 'bold'), height=1, relief=RAISED,cursor="plus",command=lambda :powerbtn(4))
    rt_button.pack(pady=10)

    root.mainloop()