import tkinter as tk
from database import db
from learning_model import neuro_net
import numpy as np
import cv2
from PIL import ImageTk, Image


def train_model():
    global mod
    list = db.get_path(data, "learn_painting", "path")
    list += db.get_path(data, "learn_picture", "path")
    val = db.get_path(data, "val_painting", "path")
    val += db.get_path(data, "val_picture", "path")
    mod = neuro_net.exec_model(list, val)


def analyse_image():
    img = cv2.imread(path_button.get(), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (50, 50))
    img = img.reshape(-1, 50, 50, 1)
    img = np.array(img)
    res = mod.predict(img)
    if res[0][0] > res[0][1]:
        result.set("Paint")
    else:
        result.set("Picture")
    print("Raw result =>", res)
    tmp = Image.open(path_button.get())
    tmp.resize((100, 100))
    p_img = ImageTk.PhotoImage(tmp)
    canvas.create_image(20, 20, anchor=tk.NW, image=p_img)
    label.pack()
    root.mainloop()


def init_gui(database):
    global data
    data = database
    global path_button
    global root
    global canvas
    global label
    global result

    root = tk.Tk()
    root.title("IRM")
    root.geometry("500x500")
    root.resizable(0, 0)
    result = tk.StringVar()
    result.set("")
    title = tk.Label(root, text="Welcome to IRM").pack()
    train_button = tk.Button(root, text="Train", width=10, command=train_model).pack()
    path_button = tk.Entry(root, width=20)
    path_button.bind("<Return>", analyse_image)
    path_button.pack()
    annalyse_button = tk.Button(root, text="Analyse", width=10, command=analyse_image).pack()
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
    label = tk.Label(root, textvariable=result)
    root.mainloop()
    return 0
