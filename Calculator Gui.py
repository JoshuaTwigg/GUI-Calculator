# noinspection PyUnresolvedReferences
import tkinter

from tkinter import *

window = Tk()

text = ""
screen_text = StringVar()


window.resizable(False, False)

# Changes default icon to calculator.png
calculator_image = PhotoImage(file="Calculator.png")
window.iconphoto(True, calculator_image)

# window size,name,background colour
window.geometry("215x375")
window.title("My Calculator")

# Frame to hold widgets
frame = Frame(window, bg="grey", bd=10, relief=RAISED)
frame.pack()


# button is clicked, then ensures the number is printed on the right-hand one after the other, displays this on screen

def button_click(number):
    global text
    text = text + str(number)
    screen_text.set(text)


# """
# pressing = it checks the global text, eval function does the math, screen displays total, text = total sets the value
# on the calculator to the answer.
# """


def equals():
    global text
    total = str(eval(text))
    screen_text.set(total)
    text = total


# sets screen to display nothing "" which is essentially clearing. Then sets the text to nothing to remove its value

def clear():
    global text
    screen_text.set("")
    text = ""


a = Button(frame, text="9", fg="white", bg="#444543", width=5, height=5, command=lambda: button_click(9))
b = Button(frame, text="8", fg="white", bg="#444543", width=5, height=5, command=lambda: button_click(8))
c = Button(frame, text="7", fg="white", bg="#444543", width=5, height=5, command=lambda: button_click(7))
d = Button(frame, text="6", fg="white", bg="#444543", width=5, height=5, command=lambda: button_click(6))
e = Button(frame, text="5", fg="white", bg="#444543", width=5, height=5, command=lambda: button_click(5))
f = Button(frame, text="4", fg="white", bg="#444543", width=5, height=5, command=lambda: button_click(4))
g = Button(frame, text="3", fg="white", bg="#444543", width=5, height=5, command=lambda: button_click(3))
h = Button(frame, text="2", fg="white", bg="#444543", width=5, height=5, command=lambda: button_click(2))
i = Button(frame, text="1", fg="white", bg="#444543", width=5, height=5, command=lambda: button_click(1))
j = Button(frame, text="0", fg="white", bg="#444543", width=5, height=3, command=lambda: button_click(0))
k = Button(frame, text="CLR", fg="white", bg="#444543", width=5, height=5, command=clear)

operation_add = Button(frame, text="+", fg="white", bg="orange", width=5, height=3, command=lambda: button_click("+"))
operation_minus = Button(frame, text="-", fg="white", bg="orange", width=5, height=3, command=lambda: button_click("-"))
operation_multiply = Button(frame, text="x", fg="white", bg="orange", width=5, height=5,
                            command=lambda: button_click("*"))
operation_divide = Button(frame, text="/", fg="white", bg="orange", width=5, height=5,
                          command=lambda: button_click("/"))
equal = Button(frame, text="=", fg="white", bg="orange", width=5, height=3, command=equals)
screen = Entry(frame, textvariable=screen_text, width=31, relief=SUNKEN, bd=3)

a.grid(row=1, column=2, pady=2, padx=2)
b.grid(row=1, column=1, pady=2, padx=2)
c.grid(row=1, column=0, pady=2, padx=2)
d.grid(row=2, column=2, pady=2, padx=2)
e.grid(row=2, column=1, pady=2, padx=2)
f.grid(row=2, column=0, pady=2, padx=2)
g.grid(row=3, column=2, pady=2, padx=2)
h.grid(row=3, column=1, pady=2, padx=2)
i.grid(row=3, column=0, pady=2, padx=2)
j.grid(row=4, column=0, pady=2, padx=2)
k.grid(row=1, column=3)

operation_add.grid(row=4, column=2, pady=2, padx=2)
operation_minus.grid(row=4, column=1, pady=2, padx=2)
operation_divide.grid(row=3, column=3, )
operation_multiply.grid(row=2, column=3)
equal.grid(row=4, column=3, pady=2, padx=2)
screen.grid(row=0, column=0, columnspan=4, pady=2, )

window.mainloop()
