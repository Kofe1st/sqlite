import sqlite3

from sqlite3 import Error


def sql_connection():

    try:
        con = sqlite3.connect('mydatabase.db')
        return con

    except Error:
        print(Error)


con = sql_connection()


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE  employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    con.commit()


sql_table(con)

#вставка данных в таблицу
def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
sql_insert(con, entities)

# обновление таблицы
def sql_update(con):
    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')

    con.commit()


sql_update(con)

#Выборка всех данных
def sql_fetch(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees')

    rows = cursorObj.fetchall()

    for row in rows:
        print(row)


sql_fetch(con)


def sql_fetch(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')

    rows = cursorObj.fetchall()

    for row in rows:
        print(row)


sql_fetch(con)

#Список таблиц
def sql_fetch(con):


    cursorObj = con.cursor()

    cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    print(cursorObj.fetchall())

sql_fetch(con)



#Удаление таблицы
def sql_fetch(con):


    cursorObj = con.cursor()

    cursorObj.execute('DROP table if exists employees')

    con.commit()

sql_fetch(con)
con.close()