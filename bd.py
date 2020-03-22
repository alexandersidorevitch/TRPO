from sqlite3 import *


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = connect("TRPO.db")  # или :memory: чтобы сохранить в RAM

conn.row_factory = dict_factory
cursor = conn.cursor()
# Создание таблицы
polya = [
    "id INTEGER PRIMARY KEY, USERNAME VARCHAR(50) NOT NULL, name VARCHAR(50) NOT NULL,grup VARCHAR(10), resuLt INTEGER NOT NULL",
    "id INTEGER PRIMARY KEY, USERNAME VARCHAR(50), password VARCHAR(50), name VARCHAR(50), grup VARCHAR(10)",
    "id INTEGER PRIMARY KEY, topic VARCHAR(50), question text",
    "id INTEGER PRIMARY KEY, question_id INTEGER, LABEL varchar(250)",
    "answer_id INTEGER PRIMARY KEY, question_id INTEGER"
]

tables = ["Records",
          "Users",
          "Questions",
          "All_Answers",
          "Correct_Answers"]
for i in range(len(tables)):
    cursor.execute("CREATE TABLE IF NOT EXISTS " + tables[i] + " ( " + polya[i] + " );")
# info = [("Pasha2001","Sanya1235","Pasha","8 class")]
# cursor.executemany("INSERT INTO users (USERNAME,password,name,grup)  VALUES (?,?,?,?)", info)
# cursor.execute("TRUCATE users")
# conn.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in cursor.fetchall():
    print(i['name'].upper())
    cursor.execute("SELECT * FROM " + i['name'])
    print(*[description[0] for description in cursor.description])
    for j in cursor.fetchall():
        print(*j)
# cursor.execute("DROP TABLE Records")
