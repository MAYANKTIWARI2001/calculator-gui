from tkinter import *
from tkinter  import Tk
import math

def click(event):
            global scvalue
            text = event.widget.cget("text")
            if text == "=":
                if scvalue.get().isdigit():
                    value = int(scvalue.get())
                else:
                   
                    value = eval(screen.get())

                    


                scvalue.set(value)
                screen.update()

            elif text == "C":
                scvalue.set("")
                screen.update()

            else:
                scvalue.set(scvalue.get() + text)
                screen.update()

root111 = Tk()
root111.geometry("644x800")
root111.title("Calculator By mayank")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root111, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

frame1 = Frame(root111, bg="grey")
button1 = Button(frame1, text="9", padx=20, pady=10, font="lucida 35 bold")
button1.pack(side=LEFT, padx=18, pady=5)
button1.bind("<Button-1>",click)

button2 = Button(frame1, text="8", padx=20, pady=10, font="lucida 35 bold")
button2.pack(side=LEFT, padx=18, pady=5)
button2.bind("<Button-1>",click)

button3 = Button(frame1, text="7", padx=20, pady=10, font="lucida 35 bold")
button3.pack(side=LEFT, padx=18, pady=5)
button3.bind("<Button-1>",click)

frame1.pack()


frame2 = Frame(root111, bg="grey")
button4 = Button(frame2, text="6", padx=20, pady=10, font="lucida 35 bold")
button4.pack(side=LEFT, padx=18, pady=5)
button4.bind("<Button-1>",click)

button5 = Button(frame2, text="5", padx=20, pady=10, font="lucida 35 bold")
button5.pack(side=LEFT, padx=18, pady=5)
button5.bind("<Button-1>",click)

button6 = Button(frame2, text="4", padx=20, pady=10, font="lucida 35 bold")
button6.pack(side=LEFT, padx=18, pady=5)
button6.bind("<Button-1>",click)

frame2.pack()


frame3 = Frame(root111, bg="grey")
button7 = Button(frame3, text="3", padx=20, pady=10, font="lucida 35 bold")
button7.pack(side=LEFT, padx=18, pady=5)
button7.bind("<Button-1>",click)

button8 = Button(frame3, text="2", padx=20, pady=10, font="lucida 35 bold")
button8.pack(side=LEFT, padx=18, pady=5)
button8.bind("<Button-1>",click)

button9 = Button(frame3, text="1", padx=20, pady=10, font="lucida 35 bold")
button9.pack(side=LEFT, padx=18, pady=5)
button9.bind("<Button-1>",click)

frame3.pack()


frame4 = Frame(root111, bg="grey")
button10 = Button(frame4, text="0", padx=23, pady=8, font="lucida 35 bold")
button10.pack(side=LEFT, padx=18, pady=5)
button10.bind("<Button-1>",click)

button11 = Button(frame4, text="-", padx=23, pady=8, font="lucida 35 bold")
button11.pack(side=LEFT, padx=18, pady=5)
button11.bind("<Button-1>",click)

button12 = Button(frame4, text="*", padx=23, pady=8, font="lucida 35 bold")
button12.pack(side=LEFT, padx=18, pady=5)
button12.bind("<Button-1>",click)

frame4.pack()


frame5 = Frame(root111, bg="grey")
button13 = Button(frame5, text="/", padx=21, pady=10, font="lucida 35 bold")
button13.pack(side=LEFT, padx=18, pady=5)
button13.bind("<Button-1>",click)



button14 = Button(frame5, text="+", padx=21, pady=10, font="lucida 35 bold")
button14.pack(side=LEFT, padx=18, pady=5)
button14.bind("<Button-1>",click)




button15 = Button(frame5, text="=", padx=21, pady=10, font="lucida 35 bold")
button15.pack(side=LEFT, padx=18, pady=5)
button15.bind("<Button-1>",click)

frame5.pack()

frame6 = Frame(root111, bg="grey")
button16 = Button(frame6, text="C", padx=18, pady=10, font="lucida 35 bold")
button16.pack(side=LEFT, padx=18, pady=5)
button16.bind("<Button-1>",click)


button17 = Button(frame6, text=".", padx=18, pady=10, font="lucida 35 bold")
button17.pack(side=LEFT, padx=18, pady=5)
button17.bind("<Button-1>",click)


button18 = Button(frame6, text="00", padx=18, pady=10, font="lucida 35 bold")
button18.pack(side=LEFT, padx=18, pady=5)
button18.bind("<Button-1>",click)


frame6.pack()
root111.mainloop()
