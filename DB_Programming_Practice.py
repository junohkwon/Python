import pymysql.cursors

def dbConn(sql, id):
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
            cursor.execute(sql,id)
            result=cursor.fetchall()
            return result
    finally:
            connection.close()

def find_Father(id):
    sql=(' select '
    	 ' t2.parent as father'
         ' from person t1, parentship t2'
         ' where t1.id = t2.child'
         ' and t1.id = %s'
         ' and exists (select 1 from marriage t3'
         '			where t2.parent = t3.husband)'
         )
    result = dbConn(sql,id)
    print(result[0]['father'])
    return result[0]['father']

def find_child(ids):
    sql=(' select t2.id from parentship t1, person t2'
         ' where t1.parent in (%s)'
         ' and t1.child = t2.id'
         ' and t2.gender = "m"'
         ' order by t2.id'
         )
    result = dbConn(sql,ids)
    print(result)


def find_child_except(id): ## 삼촌들을 가져온다.
    sql=(' select t2.id from parentship t1, person t2'
         ' where t1.parent = 35'
         ' and t1.child = t2.id'
         ' and t2.gender = "m"'
         ' and t2.id != %s'
         )
    result = dbConn(sql,father_id)

    ids = ''
    for l in result:
        for k,v in l.items():
            ids += v + ','

    find_child(ids)

'''
id를 받아들인다.
'''
input_id = input('id를 입력하세요')

'''
아버지의 id를 찾는다.
'''
father_id = find_Father(input_id)

'''
할아버지의 id를 찾는다.
'''
grandfather_id = find_Father(father_id)

'''
할아버지의 자식id를 찾아서 아버지id와 딸의 id를 제거한다.
'''
find_child_except(grandfather_id)
'''
남은 id의 자식을 찾아서 뿌린다.
'''

