import requests
from dotenv import load_dotenv
import os
import json
import smtplib


def send_email(recipient: str, room_num: str, made_by: str, reservation_id: int, from_datetime: str, until_datetime: str) -> None:
    """
    This function sends an email notification about a reservation.
    :param recipient: user's email address for sending an email notification about a reservation
    :param room_num: a room number of the room that a user wants to reserve
    :param made_by: user's name
    :param reservation_id: a reservation identification number
    :param from_datetime: from what time and date is a room reserved by a user
    :param until_datetime: until what time and date the room is reserved by user
    :return: None

    """

    FROM = 'youngjunwow@gmail.com'
    pswd = 'mwvkjurllnxxbnjg'
    TO = recipient
    SUBJECT = 'Room reservation Notification'
    TEXT = f'Reservation ID: {reservation_id}\n' \
           f'Hello {made_by}, you have reserved the the room {room_num}\n' \
           f'From: {from_datetime} ~ Until: {until_datetime}\n'\

    message = f"""From: {FROM}\nTo: {TO}\nSubject: {SUBJECT}\n\n{TEXT}"""
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(FROM, pswd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('Successfully sent the mail')
    except:
        print("Failed to send mail")


def send_sms(recipient: str, room_num: str, made_by: str, reservation_id: int, from_datetime: str, until_datetime:str) -> None:
    """
    This function sends an SMS notification about a reservation.,
    :param recipient: user's phone number for sending a message notification about a reservation
    :param room_num: a room number of the room that a user wants to reserve
    :param made_by: user's name
    :param reservation_id: a reservation identification number
    :param from_datetime: from what time and date is a room reserved by a user
    :param until_datetime: until what time and date the room is reserved by user
    :return: None
    """
    load_dotenv()
    try:
        service_plan_id = os.environ['service_plan_id']
        access_token = os.environ['access_token']
        FROM = '447520651206'
        TO = '992' + recipient
        URL = f'https://sms.api.sinch.com/xms/v1/{service_plan_id}/batches'

        header = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        message_info = {
            'from': FROM,
            'to': [TO],
            'body': f'Reservation ID: {reservation_id}\n' \
                    f'Hello {made_by}, you have reserved the the room {room_num}\n' \
                    f'From: {from_datetime} ~ Until: {until_datetime}\n'\
            }
        requests.post(URL, headers=header, data=json.dumps(message_info))

    except:
        print("Failed to send SMS")


