from tkinter import *
from backend import Database
from pynput import mouse
from pynput import keyboard

clicks = Database("Keyboards.db")  # update db with mouse
keys = Database("Keyboards.db")  # update db with keys
tkinter = Database("Keyboards.db")  # For show only


class App:

    def __init__(self, parent):

        # First Keyboards pressed
        self.total_keyboards = 0
        for x in tkinter.view():
            self.total_keyboards = self.total_keyboards + x[1]

        # Clicks label
        self.e1 = Label(parent, text="Clicks")
        self.e1.grid(row=0, column=0)

        # self.separator = Frame(height=100, width=100, relief=SUNKEN)
        # self.separator.grid(row=0, column=1)

        # Clicks number
        self.clicks = StringVar()
        self.clicks.set(tkinter.view()[-1][1])
        self.t1 = Label(parent, textvariable=self.clicks)
        self.t1.grid(row=0, column=1)

        # Keyboard Label
        self.e2 = Label(parent, text="Keyboard Pressed")
        self.e2.grid(row=1, column=0)

        # Keyboard number
        self.keyboards = StringVar()
        self.keyboards.set(self.total_keyboards)
        self.t2 = Label(parent, textvariable=self.keyboards)
        self.t2.grid(row=1, column=1)

        # Button not finished
        self.b1 = Button(parent, text="Start Recording", command=self.start_records)
        self.b1.grid(row=2, column=0, columnspan=2)

        # Label for list of keys
        self.e3 = Label(parent, text="All keys")
        self.e3.grid(row=3, column=0, columnspan=2)

        # List scroll
        self.scrollbar = Scrollbar(parent)
        self.scrollbar.grid(row=4, column=2, rowspan=4, ipady=250)

        # List of keys
        self.l1 = Listbox(parent, height=35, width=40, yscrollcommand=self.scrollbar.set)
        for row in tkinter.view():
            self.l1.insert(END, row[0] + ": " + str(row[1]))
        self.l1.grid(row=4, column=0, rowspan=4, columnspan=2)

        self.scrollbar.config(command=self.l1.yview)
        parent.resizable(FALSE, FALSE)

        # self.l1.after(0, self.update_list)  # Update values after first 1 sec
        self.e3.after(1000 * 60 * 60, self.after_1hour)
        self.e2.after(1000 * 60 * 60 * 24, self.after_1day)

    def after_1hour(self):
        tkinter.database_to_csv()
        self.e3.after(1000 * 60 * 60, self.after_1hour)

    def after_1day(self):
        tkinter.to_bokeh()
        self.e2.after(1000 * 60 * 60 * 24, self.after_1day)

    def update_list(self):  # Update values every 1 sec
        self.l1.delete(0, END)
        for row in tkinter.view():
            self.l1.insert(END, row[0] + ": " + str(row[1]))
        self.l1.config()
        self.l1.after(1000, self.update_list)

    def on_keyboard(self, key):
        keys.update(str(key))
        self.total_keyboards = 0
        for x in keys.view():
            self.total_keyboards = self.total_keyboards + x[1]
        self.keyboards.set(self.total_keyboards)

    def on_click(self, x, y, button, pressed):
        if pressed:
            clicks.update('clicked')
            self.clicks.set(clicks.view()[-1][1])

    def start_records(self):
        recording = 0
        if recording == 0:
            keyboard.Listener(on_release=self.on_keyboard).start()
            mouse.Listener(on_click=self.on_click).start()
            self.b1.config(text="Stop Recording")
            recording += 1
            print(recording)
        else:
            self.b1.config(text="Start Recording")
            keyboard.Listener(on_release=self.on_keyboard).stop()
            mouse.Listener(on_click=self.on_click).stop()
            recording -= 1
            return False


if __name__ == "__main__":
    window = Tk()
    App = App(window)
    window.mainloop()

# x = 150, 150, 'button', 'pressed'
# a = App
# a.on_click(App, 150, 150, 'button', 'pressed')
