import pymysql.cursors

def dbConn(sql):
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
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
    finally:
            connection.close()

def dbConnWithName(sql,name):
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
            cursor.execute(sql,name)
            result=cursor.fetchall()
            return result
    finally:
            connection.close()

def ExecuteNonQuery(sql):
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
            cursor.execute(sql)
            connection.commit()
    finally:
            connection.close()


def f3a():
    sql = 'select name, resident_id from student'
    result = dbConn(sql)
    print('이름', '주민등록번호')
    for l in result:
        print(l['name'], l['resident_id'])

# f3a()
print('=======================================')

def f3b():
    sql = (' select p1.name, date_format(now(),\'%Y\')-p1.year_emp work_year'
           ' from professor p1, professor p2'
           ' where p1.year_emp > p2.year_emp'
           ' and p2.name = "최성희"'
           )
    result = dbConn(sql)
    print('이름', '재직년수')
    for l in result:
        print(l['name'], int(l['work_year']))

# f3b()
print('=======================================')


def f3c():
    student_name = input('학생의 이름을 입력하세요: ')
    sql=('select'
         ' t1.name, t4.title, t2.grade'
         ' from student t1, takes t2, class t3, course t4'
         ' where 1=1'
         ' and t1.stu_id = t2.stu_id'
         ' and t2.class_id = t3.class_id'
         ' and t3.course_id = t4.course_id'
         ' and t1.name = %s')

    result = dbConnWithName(sql,student_name)

    if len(result) > 0:
        print('이름: ', result[0]['name'])
        # columns = list(result[0].keys())
        # print(columns[1],' ',columns[2])
        print('과목명', '성적')
        for l in result:
            print(l['title'], l['grade'])
    else:
        print('결과없음')
# f3c()
print('=======================================')



ExecuteNonQuery('delete from takes where stu_id = 1292001')

;

