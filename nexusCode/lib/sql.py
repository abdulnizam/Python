#!/usr/bin/python3
def create_table(db_path: str) -> str:
    try:
        cursor = db_path.execute('''CREATE TABLE IF NOT EXISTS NEXUS
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             password TEXT NOT NULL);''')

        db_path.commit()
        return 'table created.'
    except Exception as err:
        print('Error: %s' % (str(err)))


def create_new_users(db_path: str, data: list) -> None:
    try:
        sql = 'insert into NEXUS' + ' (name, email, password) VALUES ("' + \
            data['full_name'] + '" , "' + data['email'] + '", "' + data['password'] + ' ")'
        db_path.execute(sql)
        db_path.commit()
    except Exception as err:
        print('Query Failed: %s\nError: %s' % (sql, str(err)))


def update_Password(db_path: str, data: list) -> None:
    try:
        sql = 'UPDATE NEXUS SET password = "' + \
            data[1] + '" WHERE id = ' + data[0]
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
            print(row)
            results.append(
                {"id": row[0], "name": row[1], "email": row[2], "password": row[3]})

        return results
    except Exception as err:
        print('Query Failed: %s\nError: %s' % (sql, str(err)))


def select_User_By_Id(db_path: str, ids: int) -> list:
    try:
        sql = 'SELECT * from NEXUS WHERE id =' + ids
        cursor = db_path.execute(sql)
        results = []
        for row in cursor:
            results.append(
                {"id": row[0], "name": row[1], "email": row[2], "password": row[3]})

        return results
    except Exception as err:
        print('Query Failed: %s\nError: %s' % (sql, str(err)))
