import tkinter as tk
import db

db = db.init_db()


def insert_image():
    print("add image")
    insert = tk.Tk()
    insert.geometry('500x500')
    insert.resizable(0, 0)
    in_title = tk.Label(insert, text="Adding Image").pack()
    return 0


def train_model():
    print("train model")
    train = tk.Tk()
    train.geometry('500x500')
    train.resizable(0, 0)
    tr_title = tk.Label(train, text="training your model").pack()
    return 0


def analyse_image():
    print("analyse image")
    analyse = tk.Tk()
    analyse.geometry('500x500')
    analyse.resizable(0, 0)
    an_title = tk.Label(analyse, text="Image analysis").pack()


def init_gui():
    root = tk.Tk()
    root.title("IRM")
    root.geometry("500x500")
    root.resizable(0, 0)

    title = tk.Label(root, text="Welcome to IRM").pack()

# choice button
    add_button = tk.Button(root, text="Add images", width=10, command=insert_image).pack()
    train_button = tk.Button(root, text="Train", width=10, command=train_model).pack()
    analyse_button = tk.Button(root, text="Analyse", width=10, command=analyse_image).pack()

    root.mainloop()
    return 0
