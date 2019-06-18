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
        print("DB connection failed: " + str(e))


def close_db(db):
    db.close()


def create_table(db, table_name, vars):
    cur = db.cursor()
    sql = "CREATE TABLE IF NOT EXISTS " + table_name + " (id INT(10) PRIMARY KEY AUTO_INCREMENT"
    for a, b in vars:
        sql += ", " + a + " " + b + " NOT NULL"
    sql += ')'
    try:
        cur.execute(sql)
    except pymysql.Error as e:
        print("Create table failed" + str(e))


def drop_table(db, table):
    sql = "DROP TABLE " + table
    try:
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Drop table  failed: " + str(e))


def put_path(db, table, path, vars):
    var_name = []
    var_value = []
    for a, b in vars:
        var_name.append(a)
        var_value.append(b)

    sql = "INSERT INTO " + table + " ("
    for i in var_name:
        if i == var_name[-1]:
            sql += i
        else:
            sql += i + ", "
    sql += ") VALUES ("
    for i in var_value:
        if i == var_value[-1]:
            if type(i) is int:
                sql += str(i)
            elif type(i) is str:
                sql += "\'" + i + "\'"
        else:
            if type(i) is int:
                sql += str(i) + ", "
            elif type(i) is str:
                sql += "\'" + i + "\', "
    sql += ')'
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


def delete_img(db, img_id, table):
    cur = db.cursor()
    sql = "DELETE FROM " + table + "WHERE id = '%d'" % img_id
    try:
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Delete data failed: " + str(e))


def is_training(db, path, table_name):
    cur = db.cursor()
    sql = "UPDATE " + table_name + " SET tag = 1 WHERE datas = \'" + path + "\'"
    try:
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Change of training property failed: " + str(e))
