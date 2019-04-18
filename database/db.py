import mysql.connector


def init_db():
    db = mysql.connector.connect(host="localhost",
                                 user="greg",
                                 password="irmgreg",
                                 database="irmdb")
    print(db)
    return db
