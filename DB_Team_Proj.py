import pymysql.cursors

'''
common function
'''

#DB 접속 초기화
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

#Parameter를 사용하지 않고 데이터를 조회한다
def ExecuteQuery(sql):
    connection = getConn()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
    finally:
            connection.close()

#Parameter를 사용하여 데이터를 조회한다.
def ExecuteQueryWithParam(sql, param):
    connection = getConn()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, param)
            result=cursor.fetchall()
            return result
    finally:
            connection.close()

#Parameter를 사용하여 데이터를 추가/삭제한다.
def ExecuteNonQuery(sql, params):
    connection = getConn()
    try:
        with connection.cursor() as cursor:
            rowcnt = cursor.execute(sql,params)
            connection.commit()

            return rowcnt
    finally:
        connection.close()

#Parameter를 사용하여 다수의 데이터를 추가/삭제한다.
def ExecuteNonQueryMany(sql, params):
    connection = getConn()
    try:
        with connection.cursor() as cursor:
            rowcnt = cursor.executemany(sql,params)
            connection.commit()

            return rowcnt
    finally:
        connection.close()

#쿼리 결과가 존재하는지 확인한다.
def isExists(sql,params):
    dict = ExecuteQueryWithParam(sql, params)

    if len(dict) > 0:
        return True
    else:
        return False

#화면 출력함수
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
	     ' t1.id, t1.name, t1.location, t1.capacity, IFNULL(t2.cnt,0) as assigned'
         ' from building t1 left outer join (select b_id, count(*) cnt from assign group by b_id) t2 on (t1.id = t2.b_id)'
         ' order by 1'
         )
    dict = ExecuteQuery(sql)
    printData(dict)

#모든 공연정보 출력
def f2():
    sql = (' select'
           ' 	t1.id, t1.name, t1.type, t1.price, IFNULL(t2.cnt,0) booked'
           ' from performance t1 left outer join (select p_id, count(*) cnt from book group by p_id) t2 on (t1.id = t2.p_id)'
           ' order by 1'
           )
    dict = ExecuteQuery(sql)
    printData(dict)

#모든 관객정보 출력
def f3():
    sql = (' select id, name, gender, age from audience order by 1')
    dict = ExecuteQuery(sql)
    printData(dict)

#공연장 추가
def f4():
    try:
        b_name = input('Building name: ')
        b_loc = input('Building location: ')
        b_cap = int(input('Building capacity: '))

        # Validation Check - 글자길이는 200자 이하
        b_name = b_name[:200]
        b_loc = b_loc[:200]

        # Validation Check - 공연장의 정원은 1이상
        if b_cap < 1:
            print('The capacity must be greater than one')
            return

        #공연장 추가/확인
        sql=('insert into building (name,location,capacity) values(%s,%s,%s)')
        rowcnt = ExecuteNonQuery(sql,[b_name,b_loc,b_cap])

        sql=('select * from building where name=%s and location=%s and capacity=%s')
        dict = ExecuteQueryWithParam(sql,[b_name,b_loc,b_cap])

        if len(dict) == 1:
            b_id = int(dict[0]['id'])

            # 공연장 좌석 추가
            args=()
            for i in range(1, b_cap+1):
                args += ((i,b_id),)

            sql = ('insert into building_seat (id,b_id) values(%s,%s)')
            rowcnt = ExecuteNonQueryMany(sql, args)

            if rowcnt == b_cap:
                print('A building is successfully inserted')
        else:
            print('Building insert fail - Error occurred')

    except Exception as e:
        print('Error Occurred - ', e)

#공연장 삭제
def f5():
    try:
        b_id = int(input('Building ID: '))

        #Validation Check - 공연장이 존재하는지 확인
        sql=('select 1 from building where id = %s')
        dict = ExecuteQueryWithParam(sql,[b_id])

        if len(dict) > 0:
            connection = getConn()
            try:
                with connection.cursor() as cursor:
                    # building에 연결된 예매정보 삭제
                    sql = ('delete from book where p_id in ( select p_id from assign where b_id = %s)')
                    rowcnt = cursor.execute(sql, [b_id])

                    # building에 연결된 공연정보 삭제
                    sql = ('delete from assign where b_id = %s')
                    rowcnt = cursor.execute(sql, [b_id])

                    # building / building_seat(cascade delete) 삭제
                    sql = ('delete from building where id = %s')
                    rowcnt = cursor.execute(sql, [b_id])

                    connection.commit()

                    try:
                        # 정상삭제여부 확인
                        sql = ('select 1 from book where p_id in ( select p_id from assign where b_id = %s)')
                        if isExists(sql, [b_id]):
                            raise Exception('Delete Fail')
                        sql = ('select 1 from assign where b_id = %s')
                        if isExists(sql, [b_id]):
                            raise Exception('Delete Fail')
                        sql = ('select 1 from building where id = %s')
                        if isExists(sql, [b_id]):
                            raise Exception('Delete Fail')
                        print('building {0} removed'.format(b_id))
                    except:
                        print('Delete fail - Error occurred')
            except:
                connection.rollback()
                print('Error : building delete-fail (rollback)')
            finally:
                connection.close()
        else:
            print('Building does not exists : ', b_id)
    except Exception as ex:
        print('Error : ', ex)

#공연 추가
def f6():
    try:
        p_name = input('Performance name: ')
        p_type = input('Performance type: ')
        p_price = int(input('Performance price: '))

        # Validation Check - 공연이름,종류는 200자 이하
        p_name = p_name[:200]
        p_type = p_type[:200]
        # Validation Check - 가격은 0 이상
        if p_price < 0:
            print('The price must be greater than zero')
            return

        # 공연 등록
        sql=('insert into performance (name, type, price) values (%s, %s, %s)')
        rowcnt = ExecuteNonQuery(sql, [p_name, p_type, p_price])

        if rowcnt > 0:
            print('A performance is successfully inserted')
        else:
            print('Performance insert fail - Error occurred')
    except Exception as e:
        print('Error Occurred - ', e)

#공연 삭제
def f7():
    try:
        p_id = int(input('Performance ID: '))

        #Validation Check - 공연이 존재하는지 확인
        sql=('select 1 from performance where id = %s')
        dict = ExecuteQueryWithParam(sql,[p_id])

        if len(dict) > 0:
            connection = getConn()
            try:
                with connection.cursor() as cursor:
                    # 공연 예매정보 삭제
                    sql = ('delete from book where p_id = %s')
                    cursor.execute(sql, [p_id])

                    # 공연배정정보 삭제
                    sql = ('delete from assign where p_id = %s')
                    cursor.execute(sql, [p_id])

                    # 공연 삭제
                    sql = ('delete from performance where id = %s')
                    cursor.execute(sql, [p_id])

                    connection.commit()

                    try:
                        # 결과확인
                        sql = ('select 1 from book where p_id = %s')
                        if isExists(sql, [p_id]):
                            raise Exception('Delete Fail')
                        sql = ('select 1 from assign where p_id = %s')
                        if isExists(sql, [p_id]):
                            raise Exception('Delete Fail')
                        sql = ('select 1 from performance where id = %s')
                        if isExists(sql, [p_id]):
                            raise Exception('Delete Fail')
                        print('The performance has been deleted.')
                    except:
                        print('Error - performance delete fail')
            except:
                connection.rollback()
                print('Error - performance delete fail (rollback)')
            finally:
                connection.close()
        else:
            print('Performance does not exists : ', p_id)
    except Exception as ex:
        print('Error : ', ex)

#관객 추가
def f8():
    try:
        a_name = input('Audience name: ')
        a_gender = input('Audience gender: ')
        a_age = int(input('Audience age: '))

        # validation check - 200자 이하
        a_name = a_name[:200]
        # validation check - 성별은 대문자로
        a_gender = a_gender.upper()
        if a_gender != 'M' and a_gender != 'F':
            print('The gender must be "M" or "F"')
            return
        # validation check - 나이는 1살 이상
        if a_age < 1:
            print('The age must be greater than one')
            return

        sql = ('insert into audience (name, gender, age) values (%s, %s, %s)')
        rowcnt = ExecuteNonQuery(sql, [a_name, a_gender, a_age])

        if rowcnt > 0:
            print('A audience is successfully inserted')
        else:
            print('Audience insert fail - Error occurred')
    except Exception as ex:
        print('Error : ', ex)

#관객 삭제
def f9():
    try:
        a_id = int(input('Audience ID: '))

        sql = ('select 1 from audience where id = %s')
        dict = ExecuteQueryWithParam(sql, [a_id])

        if len(dict) > 0:

            connection = getConn()
            try:
                with connection.cursor() as cursor:
                    # 관객 예매정보 삭제
                    sql = ('delete from book where a_id = %s')
                    cursor.execute(sql, [a_id])

                    # 관객정보 삭제
                    sql = ('delete from audience where id = %s')
                    cursor.execute(sql, [a_id])

                    connection.commit()

                    try:
                        # 결과확인
                        sql = ('select 1 from book where a_id = %s')
                        if isExists(sql, [a_id]):
                            raise Exception('Delete Fail')
                        sql = ('select 1 from audience where id = %s')
                        if isExists(sql, [a_id]):
                            raise Exception('Delete Fail')
                        print('The audience has been deleted.')
                    except:
                        print('Error - audience delete fail')
            except:
                connection.rollback()
                print('Error - audience delete fail (rollback)')
            finally:
                connection.close()
        else:
            print('Audience does not exists : ', a_id)
    except Exception as ex:
        print('Error : ', ex)

#공연 배정
def f10():
    try:
        b_id = int(input('Building ID: '))
        p_id = int(input('Performance ID: '))

        #validation Check - 공연장 존재여부
        sql = ('select 1 from building where id = %s')
        dict = ExecuteQueryWithParam(sql, [b_id])

        if len(dict) < 1:
            print('Building does not exists')
            return

        #validation Check - 공연 존재여부
        sql = ('select 1 from performance where id = %s')
        dict = ExecuteQueryWithParam(sql, [p_id])

        if len(dict) < 1:
            print('Performance does not exists')
            return

        #validation Check - 공연장 배정여부
        sql = ('select 1 from assign where p_id = %s')
        dict = ExecuteQueryWithParam(sql, [p_id])

        if len(dict) > 0:
            print('Performance is already assigned')
            return

        sql = ('insert into assign (p_id, b_id) values (%s, %s)')
        rowcnt = ExecuteNonQuery(sql, [p_id, b_id])

        if rowcnt > 0:
            print('Successfully assign a performance')
        else:
            print('Performance assign failed - Error occurred')
    except Exception as ex:
        print('Error : ', ex)

#공연 예매
def f11():
    try:
        p_id = int(input('Performance ID: '))
        a_id = int(input('Audience ID: '))
        seats = input('Seat List: ')

        sql=('select * from audience where id = %s')
        a_dict = ExecuteQueryWithParam(sql, [a_id])

        if len(a_dict) < 1:
            print('Audience does not exists')
            return

        a_age = int(a_dict[0]['age'])

        requestSeatList = list(map(int,seats.split(',')))

        # 공연이 공연장에 배정되지 않은경우
        sql = ('select 1 from assign where p_id = %s')
        dict = ExecuteQueryWithParam(sql, [p_id])

        if len(dict) < 1:
            print('Performance does not have building')
            return
        # Performance의 최대정원수와 예약가능한 좌석번호 표시 --> 값이 없으면 매진
        sql=('	select * from (	'
             '	select	'
             '	  t1.p_id, t1.price, t1.b_id, t1.capacity, t1.seat_id, t2.a_id	'
             '	 From	'
             '		(	'
             '	        select 	'
             '				t1.id p_id, t1.name p_name, t1.price,	'
             '				t3.id b_id, t3.name b_name, t3.capacity, t4.id seat_id	'
             '			from performance t1, assign t2, building t3, building_seat t4	'
             '			where t1.id = t2.p_id	'
             '			and t2.b_id = t3.id	'
             '			and t1.id = %s	'
             '	        and t3.id = t4.b_id 	'
             '		) t1 left outer join book t2 on (t1.p_id = t2.p_id and t1.seat_id = t2.seat_number)	'
             '	 ) t0	'
             '	where t0.a_id is null	'
             '	order by p_id, seat_id	'
             )
        dict = ExecuteQueryWithParam(sql, [p_id])

        if len(dict) < 1:
            print('The seat is already full booked')
            return

        # 예약 가능한 좌석번호 리스트를 생성
        capacity = int(dict[0]['capacity'])
        ticketPrice = int(dict[0]['price'])

        if capacity < len(requestSeatList):
            print('You have exceeded the reserve capacity of the venue.')
            return


        availableSeatList = []
        for l in dict:
            availableSeatList.append(l['seat_id'])

        # 사용자가 요구한 좌석이 모두 예약가능한지 확인한다
        if all(list(map(lambda x : x in availableSeatList, requestSeatList))):
            try:
                for seatID in requestSeatList:
                    sql = ('insert into book (a_id, p_id, seat_number) values (%s,%s,%s)')
                    ExecuteNonQuery(sql,[a_id, p_id, seatID])

                    sql = ('select 1 from book where a_id = %s and p_id = %s and seat_number = %s')
                    if (not isExists(sql,[a_id, p_id, seatID])):
                        raise Exception('Insert Fail')

                print('Your reservation was successful.')
            except:
                print('Reservation fail')
                return
        else:
            print('The seat is already taken.')
            return

        # ticket 금액을 계산한다.
        totalPrice=0
        if a_age < 8: return 0
        else:
            if a_age < 13:
                totalPrice = round((ticketPrice * 0.5) ,1) * len(requestSeatList)
            elif a_age < 19:
                totalPrice = round((ticketPrice * 0.8), 1) * len(requestSeatList)
            else:
                totalPrice = ticketPrice * len(requestSeatList)


        print('Total ticket price is ', totalPrice)
    except Exception as ex:
        print('Error : ', ex)

#공연장에 배정된 공연목록 출력
def f12():
    try:
        b_id = int(input('Building ID: '))

        sql = ('select 1 from building where id = %s')
        dict = ExecuteQueryWithParam(sql, [b_id])

        if len(dict) < 1:
            print('Building does not exists')
            return

        sql = (' select'
               '	t1.p_id id, t1.p_name name, t1.p_type type, t1.ticket_price price, IFNULL(t2.cnt,0) booked'
               ' from '
               ' ('
               ' select '
               '	t3.id p_id, t3.name p_name, t3.type p_type, t3.price ticket_price'
               ' from building t1, assign t2, performance t3'
               ' where t1.id = t2.b_id'
               ' and t2.p_id = t3.id'
               ' and t1.id = %s'
               ' ) t1 left outer join (select  p_id, count(*) cnt from book group by p_id) t2 on (t1.p_id = t2.p_id)'
               ' order by 1'
                )

        dict = ExecuteQueryWithParam(sql, [b_id])
        printData(dict)
    except Exception as ex:
        print('Error : ',ex)

#공연을 예매한 관객정보 출력
def f13():
    try:
        p_id = int(input('Performance ID: '))

        sql = ('select 1 from performance where id = %s')
        dict = ExecuteQueryWithParam(sql, [p_id])

        if len(dict) < 1:
            print('Performance does not exists')
            return

        sql=('	select 	'
             '		t3.id, t3.name, t3.gender, t3.age	'
             '	from performance t1, book t2, audience t3	'
             '	where t1.id = t2.p_id	'
             '	and t1.id = %s	'
             '	and t2.a_id = t3.id	'
             '	group by t3.id, t3.name, t3.gender, t3.age	'
             '	order by t3.id	'
             )

        dict = ExecuteQueryWithParam(sql, [p_id])
        printData(dict)
    except Exception as ex:
        print('Error : ', ex)

#공연의 좌석 별 예매상황 출력
def f14():
    try:
        p_id = int(input('Performance ID: '))

        sql = ('select 1 from performance where id = %s')
        dict = ExecuteQueryWithParam(sql, [p_id])

        if len(dict) < 1:
            print('Performance does not exists')
            return

        #공연이 공연장에 배정되지 않은경우
        sql = ('select 1 from assign where p_id = %s')
        dict = ExecuteQueryWithParam(sql, [p_id])

        if len(dict) < 1:
            print('Performance does not have building')
            return

        #공연좌석 출력
        sql=('	select 	'
             '		t1.seat_number, IFNULL(t2.a_id,"") audience_id	'
             '	from 	'
             '	(	'
             '	select 	'
             '		t1.id p_id, t3.id seat_number	'
             '	from performance t1, assign t2, building_seat t3	'
             '	where t1.id = %s	'
             '	and t1.id = t2.p_id	'
             '	and t2.b_id = t3.b_id	'
             '	) t1 left outer join book t2 on (t1.p_id = t2.p_id and t1.seat_number = t2.seat_number)'
             ' order by 1'
             )

        dict = ExecuteQueryWithParam(sql, [p_id])
        printData(dict)
    except Exception as ex:
        print('Error : ', ex)

#데이터베이스 리셋 및 생성
def f16():
    reset_yn = input('The database is reset\nDo you want to proceed? ')
    if reset_yn.upper() == 'Y':
        connection = getConn()
        try:
            with connection.cursor() as cursor:

                scripts = ['drop table if exists book;',
                           'drop table if exists assign;',
                           'drop table if exists building_seat;',
                           'drop table if exists building;',
                           'drop table if exists performance;',
                           'drop table if exists audience;',
                           'create table building (	id	int auto_increment not null,    name	varchar(200),    location	varchar(200),    capacity	int unsigned,    primary key(id));',
                           'create table building_seat (	id	int not null,    b_id	int not null,    primary key(id, b_id),    foreign key(b_id) references building(id) on delete cascade);',
                           'create table performance (	id	int auto_increment not null,    name	varchar(200),    type	varchar(200),    price	int unsigned,    primary key(id));',
                           'create table audience (	id	int auto_increment not null,    name	varchar(200),    gender	char(2),    age	int unsigned,    primary key(id));',
                           'create table book (    a_id int not null,	p_id int not null,    seat_number int,    primary key(a_id,p_id,seat_number),    foreign key(a_id) references audience(id),    foreign key(p_id) references performance(id));',
                           'create table assign (	p_id int not null,	b_id int,    primary key(p_id),    foreign key(p_id) references performance(id),    foreign key(b_id) references building(id));']
                for sql in scripts:
                    rowcnt = cursor.execute(sql)
                    if rowcnt < 0 :
                        print('error')
                        break
            print('The database has been regenerated')
        except Exception as ex:
            print('Error', ex)
        finally:
            connection.close()

if __name__ == '__main__':
    while True:
        try:
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
        except Exception as ex:
            print(ex)




