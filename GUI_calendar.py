from tkinter import *
import calendar

def cal():
   yr = int(year.get())
   mn = int(month.get())
   cal = calendar.month(yr,mn)
   T1.delete(0.0,END)
   T1.insert(END,cal)


if __name__ == '__main__':
    root = Tk()
    root.geometry('350x350')
    root.title("TKINTER")
    root.config(background='#333333')
    root.resizable(0,0)

    # label
    Label(root,text=' :Monthly Calendar Generator: ',fg='white',bg='red',font=('Arial Black',10,'bold')).pack(pady=5)
    # Taking Inputs from User
    # year
    Label(root, text='YEAR: ',fg='white', bg='red', font=('Arial Black', 10, 'bold')).place(x=20,y=45)
    year = StringVar()
    yearEN = Entry(root,fg='Navy',font=('Arial Black',10,'bold'),textvariable=year)
    yearEN.place(x=80,y=45,width=60)

    # month
    Label(root, text='MONTH: ', fg='white', bg='red', font=('Arial Black', 10, 'bold')).place(x=180, y=45)
    month = StringVar()
    monthEN = Entry(root, fg='Navy', font=('Arial Black', 10, 'bold'),textvariable=month)
    monthEN.place(x=260, y= 45, width=60)

    # BUtton
    Btn1 = Button(root,text='ENTER',font=('Arial Black', 10, 'bold'),fg='yellow',bg='red',cursor='plus',command=cal)
    Btn1.pack(pady=60)

    T1 = Text(root,font=('Arial Black',15,'bold'),fg='navy',bg='yellow')
    T1.place(x=45,y=140,width=260,height=200)


    root.mainloop()

#spinbxM = Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4).pack()
# spinbxY = Spinbox(root,from_=1999,to_=2100,width=4).pack()