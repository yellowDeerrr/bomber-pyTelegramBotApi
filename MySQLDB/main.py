import pymysql
import datetime


def addLogsRequests(telegramId, userName, userInputNumber, userInputHowMuch):
    try:
        conn = pymysql.connect(
            host="containers-us-west-116.railway.app",
            port=5475,
            user="root",
            password="0yk6OVLQy05XiUK9tGKa",
            database="railway",
            cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cursor:
                now = datetime.datetime.now()
                select_now = now.strftime('%Y-%m-%d %H:%M:%S')
                insert = f"insert into usersLogsRequests (telegramId, userName, userInputNumber, userInputHowMuch, dt) values ({telegramId}, '{userName}', {userInputNumber}, {userInputHowMuch}, '{select_now}')"
                cursor.execute(insert)
                conn.commit()
        finally:
            conn.close()
    except Exception as e:
        print(e)


def checkUserInDB(telegramID, userName):
    try:
        conn = pymysql.connect(
            host="containers-us-west-116.railway.app",
            port=5475,
            user="root",
            password="0yk6OVLQy05XiUK9tGKa",
            database="railway",
            cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT userNameTelegram FROM usersRequests WHERE telegramId = {telegramID}")
                row = cursor.fetchone()
                print(row)
                if row is None:
                    return False
                else:
                    return True

        finally:
            conn.close()
    except Exception as e:
        print(e)


def checkInterval(telegramID):
    try:
        conn = pymysql.connect(
            host="containers-us-west-116.railway.app",
            port=5475,
            user="root",
            password="0yk6OVLQy05XiUK9tGKa",
            database="railway",
            cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cursor:
                print(telegramID)
                telegramId = int(telegramID)
                print(telegramId)
                cursor.execute(f"SELECT dtToEnd FROM usersRequests WHERE telegramId = {telegramId}")

                # отримуємо результат
                result = cursor.fetchone()

                datetime_value = result['dtToEnd']

                current_datetime = datetime.datetime.now()
                if datetime_value > current_datetime:
                    return False
                else:
                    now_plus_5_min = current_datetime + datetime.timedelta(minutes=5)

                    formatted_now_plus_5_min = now_plus_5_min.strftime('%Y-%m-%d %H:%M:%S')
                    print(formatted_now_plus_5_min)
                    cursor.execute(f"UPDATE usersRequests SET dtToEnd = '{formatted_now_plus_5_min}' WHERE "
                                   f"telegramId = '{telegramId}'")
                    conn.commit()
                    return True

        finally:
            conn.close()
    except Exception as e:
        print(e)


def getDt(telegramId):
    try:
        conn = pymysql.connect(
            host="containers-us-west-116.railway.app",
            port=5475,
            user="root",
            password="0yk6OVLQy05XiUK9tGKa",
            database="railway",
            cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"select dtToEnd from usersRequests where telegramId = {telegramId}")
                dt = cursor.fetchone()
                datetime_value = dt['dtToEnd']

                return datetime_value
        finally:
            conn.close()
    except Exception as e:
        print(e)


def addUserInDBRequests(userId, userName):
    try:
        conn = pymysql.connect(
            host="containers-us-west-116.railway.app",
            port=5475,
            user="root",
            password="0yk6OVLQy05XiUK9tGKa",
            database="railway",
            cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cursor:
                current_datetime = datetime.datetime.now()

                formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                print(formatted_datetime)
                insert_user = f"insert into usersRequests (telegramId, userNameTelegram, dtToEnd) values ({userId}, '{userName}', '{formatted_datetime}')"
                cursor.execute(insert_user)
                conn.commit()
        finally:
            conn.close()
    except Exception as e:
        print(e)


def checkOnline():
    try:
        conn = pymysql.connect(
            host="containers-us-west-116.railway.app",
            port=5475,
            user="root",
            password="0yk6OVLQy05XiUK9tGKa",
            database="railway",
            cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cursor:
                return None;
        finally:
            conn.close()
    except Exception as e:
        print(e)
