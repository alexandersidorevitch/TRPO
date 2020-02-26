import pymysql.cursors
from math import sin,pi
def view(connect):
    with connect.cursor() as cursor:
        cursor.execute("""SELECT * FROM users""")
        bd = cursor.fetchall()
        for d in bd:
            print(d)


def Change(connect, query: str):
    try:
        with connect.cursor() as cursor:
            cursor.execute(query)
        connect.commit()
    except:
        pass


link = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='sin',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor
                       )
# view(link)
query = "TRUNCATE `sinus`"
Change(link,query)
POV = 1
for _ in range(POV):
    x = -100
    shag = 200 / (2880*3) * POV
    for hour in range(0,24):
        time = ""
        if hour < 10:
            time += "0" + str(hour) + ":"
        else:
            time += str(hour) + ":"
        for minute in range(0,60):
            time = time[:3]
            if minute < 10:
                time += "0" + str(minute) + ":"
            else:
                time += str(minute) + ":"
            for sec in range(0,60,10):
                time = time[:6]
                if sec < 10:
                    time += "0" + str(sec)
                else:
                    time += str(sec)
                query = "INSERT INTO `sinus` (`y`, `t`) VALUES ('"+str(x*x*0.5)+"', '2020-02-20 "+time+"')"
                Change(link, query)
                x += shag

# view(link)
# query = ""
# Change(link,query)
# view(link)
link.close()
