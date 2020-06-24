import sqlite3
import pandas
from datetime import datetime as dt
import os
from bokeh.plotting import figure, output_file, save
# import threading
# lock = threading.Lock()


class Database:

    def __init__(self, db):  # Read db
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS keyboards (key text PRIMARY KEY, value integer)")
        self.cur.execute("SELECT * FROM Keyboards")
        self.rows = self.cur.fetchall()
        self.conn.commit()

    def view(self):  # Get all data from db, return as rows
        return self.rows

    def update(self, key):  # Update key +1
        # with lock:
        new_value = 0
        for row in self.rows:
            if row[0] == key:
                new_value = row[1] + 1
        conn = sqlite3.connect("Keyboards.db")
        cur = conn.cursor()
        cur.execute("UPDATE keyboards SET value=? WHERE key=?", (new_value, key))
        conn.commit()
        conn.close()
        # with sqlite3.connect("Keyboards.db") as conn:
        #     cur = conn.cursor()
        #     cur.execute("UPDATE keyboards SET value=? WHERE key=?", (new_value, key))
        #     conn.commit()

    def reset_values(self):  # Reset all values to 0 every hour
        self.cur.execute("UPDATE keyboards SET value=?", (0,))
        self.conn.commit()

    def database_to_csv(self):  # clear database per hour and create csv
        self.reset_values()
        df = pandas.DataFrame(columns=["Key", "Pressed"])
        for i in self.rows:
            df = df.append({"Key": str(i[0]), "Pressed": str(i[1])}, ignore_index=True)
        path = "C:\\Users\\matei\\Desktop\\flask_codewars\\begginer apps\\listener_app\\" + str(dt.now().day)
        if not os.path.exists(path):
            os.mkdir(path)
        df.to_csv(f"{str(dt.now().day)}/{str(dt.now().hour)}")

    def to_bokeh(self):  # create bokeh every 24h
        path = "C:\\Users\\matei\\Desktop\\flask_codewars\\begginer apps\\listener_app\\" + str(dt.now().day)
        df = pandas.DataFrame(columns=["Hour", "Total Keys"])
        file_list = []
        if not os.path.exists(path):
            os.mkdir(path)
        for filename in os.listdir(path):
            file_list.append(int(filename))

        file_list.sort()
        for name in file_list:
            df2 = pandas.read_csv(f"{path}\\{name}")
            pressed = 0
            for value in df2["Pressed"]:
                pressed += value
            df = df.append({"Hour": name, "Total Keys": pressed}, ignore_index=True)

        p = figure(plot_width=1000, plot_height=400, title="Your Presses")
        p.vbar(x=df["Hour"], width=0.5, bottom=0,
               top=df["Total Keys"], color="firebrick")

        output_file(f"{dt.now().day}{dt.now().hour}.html")
        save(p)

    def __del__(self):
        self.conn.close()


# def insert(aaa):
#     conn = sqlite3.connect("Keyboards.db")
#     cur = conn.cursor()
#     cur.executemany("INSERT INTO keyboards VALUES (?, ?)", aaa)
#     conn.commit()
#     conn.close()

# def delete(key):
#     conn = sqlite3.connect("Keyboards.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM Keyboards WHERE key=?", (key,))
#     conn.commit()
#     conn.close()


# a = Database("Keyboards.db")
# a.database_to_csv()
# a.to_bokeh()
# a.update('clicked')
# print(a.view())
# print(a.view())
