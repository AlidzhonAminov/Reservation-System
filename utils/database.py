from datetime import datetime as dt
from utils.database_connection import DatabaseConnection
from dotenv import load_dotenv
import os

from typing import Dict,List

load_dotenv()
DB_URL = os.environ["DATABASE_URI"]

# CREATING TABLE
CREATING_RESERVATIONS_TABLE = """CREATE TABLE IF NOT EXISTS reservations 
                                (id SERIAL PRIMARY KEY, 
                                room_num INTEGER, 
                                made_by TEXT, 
                                phone_num CHAR(10), 
                                email VARCHAR(255), 
                                from_datetime TIMESTAMP, 
                                until_datetime TIMESTAMP,
                                cancel INTEGER default 0);
                                """
#INSERT
INSERTING_RESERVATIONS = """INSERT INTO reservations 
                            (room_num, 
                            made_by, 
                            phone_num, 
                            email, 
                            from_datetime, 
                            until_datetime) 
                            VALUES (%s,%s,%s,%s,%s,%s) RETURNING id;
                                """
#SELECT
SELECT_RESERVATIONS = """ 
                    SELECT * FROM reservations WHERE from_datetime >= %s AND until_datetime <= %s AND NOT cancel = 1;
                    """

SELECT_ROOM_RESERVATIONS = """
                    SELECT * FROM reservations WHERE room_num = %s AND from_datetime >= %s AND until_datetime <= %s;
                    """

ROOM_RESERVATIONS = """
                    SELECT * FROM reservations WHERE room_num = %s AND NOT cancel = 1 AND (from_datetime >= %s OR until_datetime >= %s);
                    """

ROOM_AVAILABILITY_CHECK = """
                    SELECT * FROM reservations WHERE room_num = %s AND (from_datetime, until_datetime) OVERLAPS (%s, %s);
                    """

#UPDATE / ALTER
CANCEL_RESERVATION = """
                    UPDATE reservations SET cancel=1 WHERE id = %s;
                    """


def create_reservation_table() -> None:
    with DatabaseConnection(DB_URL) as connection:
        cursor = connection.cursor()
        cursor.execute(CREATING_RESERVATIONS_TABLE)


def get_all_reservation(from_datetime: str, until_datetime: str, room_num=None, specific_room=None) -> List[Dict]:
    with DatabaseConnection(DB_URL) as connection:
        cursor = connection.cursor()
        if specific_room == True:
            cursor.execute(SELECT_ROOM_RESERVATIONS, (room_num, from_datetime,until_datetime))
        else:
            cursor.execute(SELECT_RESERVATIONS, (from_datetime, until_datetime))
        reservations_info = cursor.fetchall()

        reservations_info_dict = [{'id': info[0],
                                'room_num':info[1],
                                'name':info[2],
                                'phone_num':info[3],
                                'email':info[4],
                                'from_datetime':info[5],
                                'until_datetime':info[6] ,
                                'cancel':info[7]}for info in reservations_info]
    return reservations_info_dict


def insert_reservation_info(room_num: int, name: str, from_datetime: str, until_datetime: str, phone_number: str, email_address: str):
    with DatabaseConnection(DB_URL) as connection:
        cursor = connection.cursor()

        cursor.execute(INSERTING_RESERVATIONS, (room_num, name, phone_number, email_address, from_datetime, until_datetime))
        reservation_id = cursor.fetchone()[0]
        return reservation_id


def check_before_reservation(room_num : int, from_datetime=None, until_datetime=None, first_check=None) -> List[Dict]:
    today_date = dt.today()

    with DatabaseConnection(DB_URL) as connection:
        try:
            cursor = connection.cursor()
            if first_check == True:
                string_today_date = f'{today_date.year}-{today_date.month}-{today_date.day} {today_date.hour}:{today_date.minute}'
                cursor.execute(ROOM_RESERVATIONS, (room_num,string_today_date, string_today_date))
            if first_check == False:
                cursor.execute(ROOM_AVAILABILITY_CHECK,(room_num,from_datetime,until_datetime))
            room_info = cursor.fetchall()
        except:
            room_info = None
        room_info_dict = [{'id': info[0],
                                   'room_num': info[1],
                                   'name': info[2],
                                   'phone_num': info[3],
                                   'email': info[4],
                                   'from_datetime': info[5],
                                   'until_datetime': info[6],
                                   'cancel': info[7]} for info in room_info]
    return room_info_dict


def insert_cancellation(reservation_id) -> None:
    with DatabaseConnection(DB_URL) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(CANCEL_RESERVATION, (reservation_id,))
        except TypeError:
            print('Incorrect reservation id. Please, check if you entered the correct reservation id.')