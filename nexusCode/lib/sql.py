#!/usr/bin/python3
def create_table(db_path: str):
    try:
        cursor = db_path.execute('''CREATE TABLE NEXUS
             (ID INT PRIMARY KEY,
             NAME TEXT NOT NULL,
             EMAIL TEXT NOT NULL,
             PASSWORD TEXT NOT NULL);''')

        db_path.commit()
    except Exception as err:
        print('Error: %s' % (str(err)))


def create_users(db_path: str, data: list) -> None:
    try:
        sql = 'insert into NEXUS' + ' (NAME, EMAIL, PASSWORD) VALUES ("' + \
            data['full_name'] + '" , "' + data['email'] + '", "' + data['password'] + ' ")'
        db_path.execute(sql)
        db_path.commit()
    except Exception as err:
        print('Query Failed: %s\nError: %s' % (sql, str(err)))


def update_Password(db_path: str, data: list) -> None:
    try:
        sql = 'UPDATE NEXUS SET PASSWORD = "' + \
            data[1] + '" WHERE ID = ' + data[0]
        db_path.execute(sql)
        db_path.commit()
    except Exception as err:
        print('Query Failed: %s\nError: %s' % (sql, str(err)))


def select_table(db_path: str) -> list:
    try:
        sql = 'SELECT * from NEXUS'
        cursor = db_path.execute(sql)
        results = []
        for row in cursor:
            results.append(
                {"name": row[1], "email": row[2], "password": row[3]})

        return results
    except Exception as err:
        print('Query Failed: %s\nError: %s' % (sql, str(err)))


def select_User_By_Id(db_path: str, ids: int) -> list:
    try:
        sql = 'SELECT * from NEXUS WHERE ID =' + ids
        cursor = db_path.execute(sql)
        results = []
        for row in cursor:
            results.append(
                {"name": row[1], "email": row[2], "password": row[3]})

        return results
    except Exception as err:
        print('Query Failed: %s\nError: %s' % (sql, str(err)))
