from tkinter import *
firVal = secval = operator = None
def equal():
    global secval
    secval = int(res_lbl['text'])

    if operator == '+':
        res = firVal+secval
        res_lbl.config(text=res)
    elif operator == '-':
        res = firVal - secval
        res_lbl.config(text=res)
    elif operator == '*':
        res = firVal * secval
        res_lbl.config(text=res)
    elif operator == '/':
        res = round(firVal/secval,3)
        res_lbl.config(text=res)


def  arithmatic(op):
    global firVal,operator

    firVal = int(res_lbl['text'])
    operator = op
    clear()

def getVal(val):
    current = res_lbl['text']
    new = current + str(val)
    res_lbl.config(text=new)


def clear():
    res_lbl.config(text='')

if __name__ == '__main__':
    root = Tk()
    root.geometry('280x375')
    root.resizable(0,0)
    root.title('Calculator')
    root.configure(background='#333333')

    res_lbl = Label(root,text='',fg='white',bg='#333333')
    res_lbl.config(font=('vardana',30,'bold'))
    res_lbl.grid(row=0,column=0,pady=(30),padx=(5),columnspan=20,sticky='w')

    # row1
    btn7 = Button(root,text=7,fg='white',bg='black',width=5,height=2,font=('Arial Black',13),command= lambda :getVal(7))
    btn7.grid(row=1,column=0)

    btn8 = Button(root, text=8, fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),command=lambda :getVal(8))
    btn8.grid(row=1, column=1)

    btn9 = Button(root, text=9, fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),command=lambda :getVal(9))
    btn9.grid(row=1, column=3)

    btn_add = Button(root, text='+', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),command= lambda : arithmatic('+'))
    btn_add.grid(row=1, column=4)

    # row 2
    btn4 = Button(root, text=4, fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),command=lambda :getVal(4))
    btn4.grid(row=2, column=0)

    btn5 = Button(root, text=5, fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),command=lambda :getVal(5))
    btn5.grid(row=2, column=1)

    btn6 = Button(root, text=6, fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),command=lambda :getVal(6))
    btn6.grid(row=2, column=3)

    btn_sub = Button(root, text='-', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),command= lambda : arithmatic('-'))
    btn_sub.grid(row=2, column=4)

    # row 3
    btn1 = Button(root, text=1, fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),command=lambda :getVal(1))
    btn1.grid(row=3, column=0)

    btn2 = Button(root, text=2, fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),command=lambda :getVal(2))
    btn2.grid(row=3, column=1)

    btn3 = Button(root, text=3, fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),command=lambda :getVal(3))
    btn3.grid(row=3, column=3)

    btn_mul = Button(root, text='*', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),command= lambda : arithmatic('*'))
    btn_mul.grid(row=3, column=4)

    # row 4
    btn0 = Button(root, text=0, fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),command=lambda :getVal(0))
    btn0.grid(row=4, column=0)

    btn_clear = Button(root, text='clr', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),command=clear)
    btn_clear.grid(row=4, column=1)

    btnequal = Button(root, text='=', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),command= lambda : equal())
    btnequal.grid(row=4, column=3)

    btn_div = Button(root, text='/', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),command= lambda : arithmatic('/'))
    btn_div.grid(row=4, column=4)
    root.mainloop()