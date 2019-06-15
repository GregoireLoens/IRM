import pymysql


def init_db():
    try:
        db = pymysql.connect(host="127.0.0.1",
                             user="root",
                             password="root",
                             database="test")
        print(db)

        return db
    except pymysql.Error as e:
        print("DB connection failed: "+str(e))


def close_db(db):
    db.close()


def create_table(db, table_name):
    cur = db.cursor()
    part1 = "CREATE TABLE IF NOT EXISTS "
    part2 =" (id INT(10) PRIMARY KEY AUTO_INCREMENT, datas  VARCHAR(255) NOT NULL, tag TINYINT NOT NULL);"
    sql = part1 + table_name + part2
    try:
        cur.execute(sql)
    except pymysql.Error as e:
        print("Create table failed" + str(e))


def drop_table(db):
    try:
        cur = db.cursor()
        cur.execute("DROP TABLE imgs")
        db.commit()
    except pymysql.Error as e:
        print("Drop table  failed: " + str(e))


def put_path(db, table, path):
    sql = "INSERT INTO " + table + " (datas, tag) VALUES (\'" + path + "\', 0)"
    try:
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Fail to insert the img" + str(e))


def get_path(db, table):
    cur = db.cursor()
    sql = "SELECT datas FROM " + table
    try:
        cur.execute(sql)
        results = cur.fetchall()
        return results
    except pymysql.Error as e:
        print("Fetch data failed: " + str(e))


def delete_img(db, img_id):
    cur = db.cursor()
    sql = "DELETE FROM imgs WHERE id = '%d'" % img_id
    try:
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Delete data failed: " + str(e))


def is_training(db, path, table_name):
    cur = db.cursor()
    sql = "UPDATE " + table_name + " SET tag = 1 WHERE datas = \'" + path + "\';"
    try:
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Change of training property failed: " + str(e))
