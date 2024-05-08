from tkinter import *

firstval = secondval = operator = None


def equal():
    global secondval, firstval
    secondval = int(res_lbl['text'])

    clear()  # to clear display
    res = 0

    # perform arithematic operation

    if operator == '+':
        res = firstval + secondval

    elif operator == '-':
        res = firstval - secondval

    elif operator == '*':
        res = firstval * secondval

    elif operator == '/':
        try:
            res = firstval / secondval

        except Exception as msg:
            res = "Error";

    res_lbl.config(text=res, font=('vardana', 30, 'bold'))
    firstval = res


def arithmatic(op):
    global firstval, operator

    firstval = int(res_lbl['text'])  # convert into integer
    operator = op
    clear()


def getVal(val):
    current = res_lbl['text']
    new = current + str(val)
    res_lbl.config(text=new)

    return


def clear():
    res_lbl.config(text='')


if __name__ == '__main__':
    root = Tk()

    root.title("Calculator")
    root.geometry("280x375")
    root.resizable(0, 0)
    root.configure(background='#333')

    res_lbl = Label(root, text='', fg='white', bg='#333')
    res_lbl.config(font=('vardana', 30, 'bold'))
    res_lbl.grid(row=0, column=0, padx=(5), pady=(30), columnspan=5, sticky='e')

    # row 1
    btn7 = Button(root, text='7', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(7))
    btn7.grid(row=1, column=0)

    btn8 = Button(root, text='8', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(8))
    btn8.grid(row=1, column=1)

    btn9 = Button(root, text='9', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(9))
    btn9.grid(row=1, column=2)

    addBtn = Button(root, text='+', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),
                    command=lambda: arithmatic('+'))
    addBtn.grid(row=1, column=4)

    # row 2

    btn4 = Button(root, text='4', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(4))
    btn4.grid(row=2, column=0)

    btn5 = Button(root, text='5', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(5))
    btn5.grid(row=2, column=1)

    btn6 = Button(root, text='6', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(6))
    btn6.grid(row=2, column=2)

    minusBtn = Button(root, text='-', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),
                      command=lambda: arithmatic('-'))
    minusBtn.grid(row=2, column=4)

    # row3
    # row 1
    btn1 = Button(root, text='1', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(1))
    btn1.grid(row=3, column=0)

    btn2 = Button(root, text='2', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(2))
    btn2.grid(row=3, column=1)

    btn3 = Button(root, text='3', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(3))
    btn3.grid(row=3, column=2)

    multiplyBtn = Button(root, text='*', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),
                         command=lambda: arithmatic('*'))
    multiplyBtn.grid(row=3, column=4)

    # row4
    # row 1
    btn0 = Button(root, text='0', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                  command=lambda: getVal(0))
    btn0.grid(row=4, column=0)

    btnclr = Button(root, text='clr', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                    command=clear)
    btnclr.grid(row=4, column=1)

    btnequal = Button(root, text='=', fg='white', bg='black', width=5, height=2, font=('Arial Black', 13),
                      command=equal)
    btnequal.grid(row=4, column=2)

    btndivi = Button(root, text='/', fg='white', bg='#90A4AE', width=5, height=2, font=('Arial Black', 13),
                     command=lambda: arithmatic('/'))
    btndivi.grid(row=4, column=4)

    root.mainloop()