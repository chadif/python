import mysql.connector as mysql


def connect(db_name):
    try:
        return mysql.connect(
            host='localhost',
            user='root',
            passwd='mysql1',
            database=db_name)
    except Error as e:
        print(e)
        return None


if __name__ == '__main__':
    db = connect("canadian_post")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM address")
    addresses = cursor.fetchall()
    print(addresses)

    db.close()
