import pymysql.cursors

'''
common function
'''

def getConn():
    connection = pymysql.connect(
        host='147.46.215.246',
        port=33060,
        user='jokwon79@gmail.com',
        password='Pa$$w0rd',
        db='ds2_db13',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection

def ExecuteQuery(sql):
    connection = getConn()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
    finally:
            connection.close()

def ExecuteQueryWithParam(sql, param):
    connection = getConn()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, param)
            result=cursor.fetchall()
            return result
    finally:
            connection.close()

def ExecuteNonQuery(sql, params):
    connection = getConn()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql,params)
            connection.commit()
    finally:
        connection.close()

def isExists(sql,params):
    dict = ExecuteQueryWithParam(sql, params)

    if len(dict) > 0:
        return True
    else:
        return False

def printData(data):
    print("-------------------------------------------------------------------------------------")
    if len(data)==0:
        print("No data")
    else:
        keys=list(data[0].keys())
        nitem=len(keys)
        for i in range(nitem):
            if keys[i]=='name':
                print('{0: <30}'.format(keys[i]),end='')
            else:
                print('{0: <13}'.format(keys[i]),end='')
        print()
        print("-------------------------------------------------------------------------------------")
        for row in data:
            for i in range(nitem):
                if keys[i]=='name':
                    print('{0: <30}'.format(row[keys[i]]),end='')
                else:
                    print('{0: <13}'.format(row[keys[i]]),end='')
            print()
    print("-------------------------------------------------------------------------------------")
    print()
    print()

'''
logic function
'''

#모든 공연장 정보 출력
def f1():
    sql=(' select'
	     ' t1.id, t1.name, t1.location, t1.capacity, t2.cnt as assigned'
         ' from building t1 left outer join (select b_id, count(*) cnt from assign group by b_id) t2 on (t1.id = t2.b_id)'
         )
    dict = ExecuteQuery(sql)
    printData(dict)

#모든 공연정보 출력
def f2():
    sql = (' select'
           ' 	t1.id, t1.name, t1.type, t1.price, IFNULL(t2.cnt,0) booked'
           ' from performance t1 left outer join (select p_id, count(*) cnt from book group by p_id) t2 on (t1.id = t2.p_id)'
           )
    dict = ExecuteQuery(sql)
    printData(dict)

#모든 관객정보 출력
def f3():
    sql = (' select id, name, gendor, age from audience')
    dict = ExecuteQuery(sql)
    printData(dict)

#공연장 추가
def f4():
    try:
        b_name = input('Building name: ')
        b_loc = input('Building location: ')
        b_cap = int(input('Building capacity: '))

        #validation check
        b_name = b_name[:200]
        b_loc = b_loc[:200]
        if b_cap < 1:
            print('The capacity must be greater than one')
            return

        sql=('insert into building (name,location,capacity) values(%s,%s,%s)')

        ExecuteNonQuery(sql,[b_name,b_loc,b_cap])

        sql=('select * from building where name=%s and location=%s and capacity=%s')
        dict = ExecuteQueryWithParam(sql,[b_name,b_loc,b_cap])

        if len(dict) == 1:
            print('A building is successfully inserted')
        else:
            print('Building insert fail - Error occurred')
    except Exception as e:
        print('Error Occurred - ', e)

#공연장 삭제
def f5():
    b_id = int(input('Building ID: '))

    sql=('select * from building where id = %s')
    dict = ExecuteQueryWithParam(sql,[b_id])

    if len(dict) == 1:

        connection = getConn()
        try:
            with connection.cursor() as cursor:
                # building에 연결된 book 삭제
                sql = ('delete from book where p_id in ( select p_id from assign where b_id = %s)')
                cursor.execute(sql, [b_id])

                # assign 삭제
                sql = ('delete from assign where b_id = %s')
                cursor.execute(sql, [b_id])

                # building삭제
                sql = ('delete from building where id = %s')
                cursor.execute(sql, [b_id])

                connection.commit()
        except:
            connection.rollback()
        finally:
            connection.close()

        try:
            #결과확인
            sql = ('select * from book where p_id in ( select p_id from assign where b_id = %s)')
            if isExists(sql, [b_id]):
                raise Exception('Delete Fail')
            sql = ('select * from assign where b_id = %s')
            if isExists(sql, [b_id]):
                raise Exception('Delete Fail')
            sql = ('select * from building where id = %s')
            if isExists(sql, [b_id]):
                raise Exception('Delete Fail')
        except:
            print('Delete fail - Error occurred')


    else:
        print('Building does not exists : ', b_id)

#공연 추가
def f6():
    try:
        p_name = input('Performance name: ')
        p_type = input('Performance type: ')
        p_price = int(input('Performance price: '))

        # validation check
        p_name = p_name[:200]
        p_type = p_type[:200]
        if p_price < 0:
            print('The price must be greater than zero')
            return

        sql=('insert into performance (name, type, price) values (%s, %s, %s)')

        ExecuteNonQuery(sql, [p_name, p_type, p_price])

        sql = ('select * from performance where name=%s and type=%s and price=%s')
        dict = ExecuteQueryWithParam(sql, [p_name, p_type, p_price])

        if len(dict) == 1:
            print('A performance is successfully inserted')
        else:
            print('Performance insert fail - Error occurred')
    except Exception as e:
        print('Error Occurred - ', e)

#공연 삭제
def f7():
    p_id = int(input('Performance ID: '))

    sql=('select * from performance where id = %s')
    dict = ExecuteQueryWithParam(sql,[p_id])

    if len(dict) == 1:

        connection = getConn()
        try:
            with connection.cursor() as cursor:
                # performance 연결된 book 삭제
                sql = ('delete from book where p_id = %s')
                cursor.execute(sql, [p_id])

                # assign 삭제
                sql = ('delete from assign where p_id = %s')
                cursor.execute(sql, [p_id])

                # performance 삭제
                sql = ('delete from performance where id = %s')
                cursor.execute(sql, [p_id])

                connection.commit()
        except:
            connection.rollback()
        finally:
            connection.close()

        try:
            #결과확인
            sql = ('select * from book where p_id = %s')
            if isExists(sql, [p_id]):
                raise Exception('Delete Fail')
            sql = ('select * from assign where p_id = %s')
            if isExists(sql, [p_id]):
                raise Exception('Delete Fail')
            sql = ('select * from performance where id = %s')
            if isExists(sql, [p_id]):
                raise Exception('Delete Fail')
        except:
            print('Delete fail - Error occurred')
    else:
        print('Performance does not exists : ', p_id)

#관객 추가
def f8():
    a_name = input('Audience name: ')
    a_gender = input('Audience gender: ')
    a_age = int(input('Audience age: '))

    # validation check
    a_name = a_name[:200]
    a_gender = a_gender.upper()
    if a_gender != 'M' and a_gender != 'F':
        print('The gender must be "M" or "F"')
        return

    if a_age < 1:
        print('The age must be greater than one')
        return

    sql = ('insert into audience (name, gender, age) values (%s, %s, %s)')

    ExecuteNonQuery(sql, [a_name, a_gender, a_age])

    sql = ('select * from audience where name=%s and gender=%s and age=%s')
    dict = ExecuteQueryWithParam(sql, [a_name, a_gender, a_age])

    if len(dict) == 1:
        print('A audience is successfully inserted')
    else:
        print('Audience insert fail - Error occurred')

#관객 삭제
def f9():
    pass

#공연 배정
def f10():
    pass

#공연 예매
def f11():
    pass

#공연장에 배정된 공연목록 출력
def f12():
    pass

#공연을 예매한 관객정보 출력
def f13():
    pass

#공연의 좌석 별 예매상황 출력
def f14():
    pass

#데이터베이스 리셋 및 생성
def f16():
    reset_yn = input('The database is reset\nDo you want to proceed? ')
    if reset_yn.upper() == 'Y':
        pass

if __name__ == '__main__':
    while True:
        print('==================================================')
        print('1. print all buildings')
        print('2. print all performances')
        print('3. print all audiences')
        print('4. insert a new building')
        print('5. remove a building')
        print('6. insert a new performance')
        print('7. remove a performance')
        print('8. insert a new audience')
        print('9. remove an audience')
        print('10. assign a performance to a building')
        print('11. book a performance')
        print('12. print all performances which assigned at a building')
        print('13. print all audiences who booked for a performance')
        print('14. print ticket booking status of a performance')
        print('15. exit')
        print('16. reset database')
        print('==================================================')
        idx = int(input('Select your action: '))

        if idx == 15:
            print('Bye!')
            break;
        else:
            if idx == 1:
                f1()
            elif idx == 2:
                f2()
            elif idx == 3:
                f3()
            elif idx == 4:
                f4()
            elif idx == 5:
                f5()
            elif idx == 6:
                f6()
            elif idx == 7:
                f7()
            elif idx == 8:
                f8()
            elif idx == 9:
                f9()
            elif idx == 10:
                f10()
            elif idx == 11:
                f11()
            elif idx == 12:
                f12()
            elif idx == 13:
                f13()
            elif idx == 14:
                f14()
            elif idx == 16:
                f16()



