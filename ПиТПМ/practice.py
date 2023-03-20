import sqlite3
from sqlite3 import Error

#Создание БД
def sql_connection():
    try:
        con = sqlite3.connect('city.db')
        return con

    except Error:
        print(Error)

#Создание таблицы
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE street(id integer PRIMARY KEY, name_street text)")
    con.commit()

#Вставка данных в таблицу
def sql_insert_street(con, entities):
    cursorObj = con.cursor()
    cursorObj.executemany('INSERT INTO street(id, name_street) VALUES(?, ?)', entities)
    con.commit()


entities = (1, "Кирова"), (2, "Чернышевского"), (3, "Северная"), (4, "Герцена"), (5, "Зосимовская")

con = sql_connection()

sql_table(con)
sql_insert_street(con, entities)

con.close()