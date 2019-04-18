import tkinter as tk


def insert_image(path):
    print(path.get())
    return path


def init_gui():
    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(0, 0)

    title = tk.Label(root, text="Welcome to IRM")
    title.pack()

# path field ######
    path = tk.StringVar()
    path_entry = tk.Entry(root, textvariable=path).pack()
    path_button = tk.Button(root, text="confirm", width=10, command=lambda: insert_image(path)).pack()

    root.mainloop()
    return 0
