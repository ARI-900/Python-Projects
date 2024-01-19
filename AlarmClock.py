from tkinter import  *
import  datetime
import time
import  winsound

def Alarm(set_alarm):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%H:%M:%S")

        if current_time != set_alarm:
            print(current_time)
        else:
            print("Time to wake up ...")
            for i in range(20):
                time.sleep(1)
                winsound.PlaySound("sound_wav",winsound.SND_ASYNC)
            return


def SetAlarm():
    set_alarm = hour.get() + ":" + min.get() + ":" + sec.get()
    Alarm(set_alarm)

if __name__ == '__main__':
    clk = Tk()
    clk.title("Alarm Clock")
    clk.geometry("400x250")
    clk.resizable(0,0)

    Fm1 = Frame(clk,width=400,height=50,bg='#333333')
    Fm1.propagate(0)
    Fm1.pack()

    Label(Fm1,text='When to Wake you up',font=('Arial Black',12,'bold'),fg='white',bg='#333333',highlightbackground='Yellow',highlightthickness=2).pack(pady=10)

    # Label Hours - Min - Sec
    Label(clk,text='Hour',font=('Arial Black',15,'bold'),).place(x=80,y=60)
    Label(clk,text='Min',font=('Arial Black',15,'bold'),).place(x=180,y=60)
    Label(clk,text='Sec',font=('Arial Black',15,'bold'),).place(x=280,y=60)

    # Taking User Input hour - min - sec

    hour = StringVar()
    min = StringVar()
    sec = StringVar()

    Entry(clk,font=('Arial Black',15,'bold'),bg='Navy',fg='white',highlightthickness=2,highlightbackground='red',textvariable=hour).place(x=80,y=100,height=40,width=50)
    Entry(clk,font=('Arial Black',15,'bold'),bg='Navy',fg='white',highlightthickness=2,highlightbackground='red',textvariable=min).place(x=180,y=100,height=40,width=50)
    Entry(clk,font=('Arial Black',15,'bold'),bg='Navy',fg='white',highlightthickness=2,highlightbackground='red',textvariable=sec).place(x=280,y=100,height=40,width=50)

    btn = Button(clk,text='Set Alarm',bg='white',fg='red',relief=RAISED,font=("Vardana",13,'bold'),
                 command=SetAlarm).place(x=150,y=150,height=40,width=100)

    clk.mainloop()