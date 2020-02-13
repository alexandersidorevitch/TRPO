import pymysql.cursors

def view(connect):
    with connect.cursor() as cursor:
        cursor.execute("""SELECT * FROM users""")
        bd = cursor.fetchall()
        for d in bd:
            print(d)
def Change(connect,query:str):
    with connect.cursor() as cursor:
        cursor.execute(""""""+query+"""""")
    connect.commit()
link = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password='root',
                       db = 'test',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor
                       )
# view(link)
query = "DELETE FROM users WHERE id > 6520;"
Change(link,query)
view(link)
query =""
# Change(link,query)
view(link)
link.close()