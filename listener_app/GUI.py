from tkinter import *

# import pandas
# import KeyboardListener
# import MouseListener

window = Tk()

clicks = 0
keyboards = 0


def reader():
    global clicks, keyboards
    clicks = 0
    keyboards = 0

    with open("log.txt", "r") as file:
        my_array = [[value.strip() for value in row.split(",")] for row in file]
        for value in my_array:

            if value[0] == "clicked":
                clicks += 1
            else:
                keyboards += 1
    window.after(1, reader)


window.after(0, reader)
e1 = Label(window, text="Clicks")
e1.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t1.insert(INSERT, clicks)
t1.config(state="disabled")
t1.grid(row=0, column=1)

e2 = Label(window, text="Keyboard Pressed")
e2.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.insert(INSERT, keyboards)
t2.config(state="disabled")
t2.grid(row=1, column=1)

b1 = Button(window, text="Start Recording")
b1.grid(row=2, column=0, columnspan=2)

e3 = Label(window, text="All keys")
e3.grid(row=3, column=0, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=4, column=2, rowspan=4, ipady=250)

l1 = Listbox(window, height=35, width=40, yscrollcommand=scrollbar.set)
with open("log.txt", "r") as file:
    my_array = [[value.strip() for value in row.split(",")] for row in file]
    x = 0
    for value in my_array:
        l1.insert(x, value)
        x += 1
l1.grid(row=4, column=0, rowspan=4, columnspan=2)

scrollbar.config(command=l1.yview)

window.resizable(FALSE, FALSE)
window.mainloop()


try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class Timer:
    def __init__(self, parent):
        # variable storing time
        self.seconds = 0
        # label displaying time
        self.label = tk.Label(parent, text="0 s", font="Arial 30", width=10)
        self.label.pack()
        # start the timer
        self.label.after(1000, self.refresh_label)

    def refresh_label(self):
        """ refresh the content of the label every second """
        # increment the time
        self.seconds += 1
        # display the new time
        self.label.configure(text="%i s" % self.seconds)
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        self.label.after(1000, self.refresh_label)

if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()