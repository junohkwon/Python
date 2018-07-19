import pymysql.cursors

connection = pymysql.connect(
    host='s.snu.ac.kr',
    user='E5',
    password='Pa$$w0rd',
    db='E5',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        sql='select * from student'
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)

finally:
        connection.close()