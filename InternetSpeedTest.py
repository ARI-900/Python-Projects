#
from tkinter import *
import speedtest as spd
def speedTest():
    sp = spd.Speedtest()
    sp.get_servers()
    down = sp.download()/(10**6)
    down = str(round(down,2))+' Mbps'

    up = sp.upload()/(10**6)
    up = str(round(up))+' Mbps'

    IS_I.config(text=down)
    US_I.config(text=up)


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x500')
    root.title("Interner Speed Test")
    root.resizable(0,0)
    root.config(background='#333333')

    # heading
    Label(root,text=': Internet Speed Indicator :',font=('Time New Roman',20,'bold'),fg='black',width=380).pack(pady=8,padx=10)

    # speed indiaccator
    IS = Label(root, text='Download Speed Test', font=('Time New Roman', 18, 'bold'), fg='orange',bg='#CCD1D1' )
    IS.place(x= 50,y=69,width=300)
    IS_I = Label(root, text='00', font=('Time New Roman', 20, 'bold'), fg='navy',bg='#AED6F1' )
    IS_I.place(x=50 ,y=129,height= 50,width=300)
    US = Label(root, text='Upload Speed Test', font=('Time New Roman', 18, 'bold'), fg='orange', bg='#CCD1D1')
    US.place(x= 50,y= 210,width=300)
    US_I = Label(root, text='00', font=('Time New Roman', 20, 'bold'), fg='black',bg='#AED6F1')
    US_I.place(x=50 ,y=280,height= 50,width=300)

    # BUtton
    btn = Button(root,text='Check Speed',font=('Time New Roman', 15, 'bold'),relief=RAISED,bg='red',fg='yellow',command=speedTest)
    btn.place(x=110,y=390,height=40,width=170)


    root.mainloop()
