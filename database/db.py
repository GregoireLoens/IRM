import pymysql


def init_db():
    try:
        db = pymysql.connect(host="localhost",
                             user="root",
                             password="DiaMiao415",
                             database="irmdb")
        print(db)

        return db
    except pymysql.Error as e:
        print("DB connection failed: "+str(e))


def close_db(db):
    db.close()


def creat_table(db):
    cur = db.cursor()
    sql = """CREATE TABLE IF NOT EXIST 'IMGS' (
                         IMG_id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                         IMG_data  MEDIUMBLOB NOT NULL,
                         IMG_tag INT(1))"""
    cur.execute(sql)


def drop_table(db):
    try:
        cur = db.cursor()
        cur.execute ("DROP TABLE IMGS")
    except pymysql.Error as e:
        print("Drop table  failed: " + str(e))
    db.commit()


def insert_img(db, url, tag):
    try:
        f = open(url, "rb")
        b = f.read()
        f.close()
    except IOError as e:
        print("Fail to open the img" + str(e))

    try:
        cur = db.cursor()
        cur.execute("INSERT INTO IMGS (IMG_data, IMG_tag) VALUES (%s, %d)", pymysql.Binary(b),tag)
        db.commit()
    except pymysql.Error as e:
        db.rollback()
        print("Fail to insert the img" + str(e))


def query_all_imgs(db):
    cur = db.cursor()
    sql = "SELECT * FROM IMGS"
    try:
        cur.execute(sql)
        results = cur.fetchall()
        return results
    except pymysql.Error as e:
        print("Fetch data failed: " + str(e))


def delete_img(db, img_id):
    cur = db.cursor()
    sql = "DELETE FROM IMGS WHERE IMG_id = '%d'" % img_id
    try:
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Delete data failed: " + str(e))
