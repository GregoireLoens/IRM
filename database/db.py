import pymysql


def init_db():
    try:
        db = pymysql.connect(host="127.0.0.1",
                             user="loens_g",
                             password="Loens_g59",
                             database="irm")
        print(db)

        return db
    except pymysql.Error as e:
        print("DB connection failed: " + str(e))


def close_db(db):
    db.close()

# db --> db object to access our current database
# table_name --> name of the table we are working on
# vars --> list of the variable and their type formatted
# like this [(variable name, variable type), (variable name, variable type)]


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

# db --> object to access our database
# table --> name of the table we want to access


def drop_table(db, table):
    sql = "DROP TABLE " + table
    try:
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Drop table  failed: " + str(e))

#db --> object to access our database
#table --> the name of the table we want to access
#vars --> all of the variable we want to add and their corresponding value formated
#         like this [(column name, column value), (column name, column value)]


def put_path(db, table, vars):
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

# db --> object used to access the database
# table --> name of the table we want to perform the operation on
# column --> name of the column we want to retrieve the data from


def get_path(db, table, column):
    cur = db.cursor()
    sql = "SELECT " + column + " FROM " + table
    try:
        cur.execute(sql)
        results = cur.fetchall()
        return results
    except pymysql.Error as e:
        print("Fetch data failed: " + str(e))

# db --> object used to access the database
# img_id --> id of the image we want to delete
# table --> name of the table we want to perform the operation on


def delete_img(db, img_id, table):
    cur = db.cursor()
    sql = "DELETE FROM " + table + "WHERE id = '%d'" % img_id
    try:
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Delete data failed: " + str(e))


# db --> object used to access the database
# path --> path of the image you want to change
# table_name --> name of the table we want to perform operation on
# tag_column --> column where we want the image to be marked as trained
# path_column --> column where the path is stocked


def is_training(db, path, table_name, tag_column, path_column):
    cur = db.cursor()
    sql = "UPDATE " + table_name + " SET " + tag_column + " = 1 WHERE " + path_column + " = \'" + path + "\'"
    try:
        cur.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print("Change of training property failed: " + str(e))
