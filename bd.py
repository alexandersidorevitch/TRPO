from sqlite3 import *

# Режим отображение таблиц
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
conn = connect("TRPO.db")  # подлкючение к БД

conn.row_factory = dict_factory

cursor = conn.cursor()

# Создание таблиц
polya = [
    "id INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME VARCHAR(50) NOT NULL, result FLOAT NOT NULL",
    "id INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL, name VARCHAR(50) NOT NULL, grup VARCHAR(10) NOT NULL" ,
    "id INTEGER PRIMARY KEY AUTOINCREMENT, topic VARCHAR(50) NOT NULL, question text NOT NULL",
    "id INTEGER PRIMARY KEY AUTOINCREMENT, question_id INTEGER NOT NULL, LABEL varchar(250) NOT NULL",
    "answer_id INTEGER PRIMARY KEY AUTOINCREMENT, question_id INTEGER NOT NULL"
]

tables = ["Records",
          "Users",
          "Questions",
          "All_Answers",
          "Correct_Answers"]

for i in range(len(tables)):
    cursor.execute("CREATE TABLE IF NOT EXISTS " + tables[i] + " ( " + polya[i] + " );")

# info = [("Sasha","68")]
# cursor.executemany("INSERT INTO records (USERNAME,result)  VALUES (?,?)", info)
# conn.commit()




# Вывод всего из всех таблиц
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in cursor.fetchall():
    if i['name'] != "sqlite_sequence":
        print(i['name'].upper())
        cursor.execute("SELECT * FROM " + i['name'])
        print(*[description[0] for description in cursor.description])
        for j in cursor.fetchall():
            print(*j.values())
        print("\n")
        # cursor.execute("DROP TABLE " + i['name'])


# весь вывод из 2 таблиц 'Users' и 'Records'
cursor.execute("SELECT * FROM users JOIN records ON users.id = records.id")
print(*[description[0] for description in cursor.description])
for j in cursor.fetchall():
    print(*j.values())