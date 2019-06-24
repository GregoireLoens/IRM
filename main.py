from GUI import gui
from database import db
from os import listdir
from os.path import isfile, join


def create_db():
    database = db.init_db()
    db.create_table(database, "learn_painting", [("path", "VARCHAR(480)"), ("learned", "TINYINT")])
    db.create_table(database, "learn_picture", [("path", "VARCHAR(480)"), ("learned", "TINYINT")])
    db.create_table(database, "val_painting", [("path", "VARCHAR(480)")])
    db.create_table(database, "val_picture", [("path", "VARCHAR(480)")])
    for elem in listdir("./painting"):
       db.put_path(database, "learn_painting", [("path", join("./painting", elem)), ("learned", 0)])
    for elem in listdir("./picture"):
       db.put_path(database, "learn_picture", [("path", join("./picture", elem)), ("learned", 0)])
    for elem in listdir("./validation_paint"):
       db.put_path(database, "val_painting", [("path", join("./validation_paint", elem))])
    for elem in listdir("./validation_picture"):
       db.put_path(database, "val_picture", [("path", join("./validation_picture", elem))])
    return database


if __name__ == '__main__':
    data = create_db()
    gui.init_gui(database=data)
