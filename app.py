from utils import database
from utils import UserInputHandler


USER_CHOICE = """
Enter:
 '1' to check reservation of a specific room or all rooms.
 '2' to make a reservation.
 '3' cancel reservation.
 'q' to quit.
Your choice: """


def menu():
    database.create_reservation_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == '1':
            check_reservation()
        elif user_input == '2':
            make_reservation()
        elif user_input == '3':
            cancel_reservation()

        user_input = input(USER_CHOICE)


def check_reservation():

    specific_room = input('Are you interested in a specific room? Enter Yes or No: ')
    specific_room = specific_room.lower()
    if specific_room == 'yes':
        room_num = UserInputHandler.__room_info(return_type='check')
        from_date = UserInputHandler.__from_date_info(return_type='check')
        until_date = UserInputHandler.__until_date_info(from_date,return_type='check')
        data = database.get_all_reservation(from_date, until_date, room_num, specific_room=True)
        if bool(data) == True:
            print(f'The reservation information for the room {room_num}')
            print('---------------------------------------------------')
            for reservation in data:
                print(f"Reserved by {reservation['name']} from: {reservation['from_datetime']} until: {reservation['until_datetime']}")
            print(f'The room {room_num} is available for the reservation except for the listed above times and dates.')
        else:
            print('This room does not have any reservations.')

    else:
        from_date = UserInputHandler.__from_date_info(return_type='check')
        until_date = UserInputHandler.__until_date_info(from_datetime = from_date,return_type ='check')
        data = database.get_all_reservation(from_date, until_date)
        sorted_data_dict = sorted(data, key=lambda i: i['room_num'], reverse=False)
        if bool(data) == True:
            print(f'Below is the listed reservation record of all rooms.')
            print('---------------------------------------------------')
            for reservation in sorted_data_dict:
                print(f"The room {reservation['room_num']} is reserved by {reservation['name']} from: {reservation['from_datetime']} until: {reservation['until_datetime']}")
        else:
            print('This room does not have any reservations.')


def make_reservation():

    #Room information
    room_num = UserInputHandler.__room_info()

    #Checking room reservations
    reservation_data = database.check_before_reservation(room_num, first_check=True)
    if bool(reservation_data) == True:
        print(f'The reservation information for the room {room_num}: ')
        print('---------------------------------------------------')
        for reservation in reservation_data:
            print(f"Reserved by {reservation['name']} from: {reservation['from_datetime']} until: {reservation['until_datetime']}")
        print(f'The room {room_num} is available for the reservation except for the listed above times and dates.')
    else:
        print('This room does not have any reservations. You can reserve this room for any time and date.')

    #Getting the name
    name = str(input('Enter your name: ')).upper()

    #Getting infromation  from when the room is needed
    from_datetime = UserInputHandler.__from_date_info()

    #Getting infromation until when the room is needed
    until_datetime = UserInputHandler.__until_date_info(from_datetime)


    #Getting information about a phone number
    phone_number = UserInputHandler.__phone_number_info()

    #Getting information about an email address
    email_address = UserInputHandler.__email_address_info()

    #Checking if the room is available for the given date and time.
    check_before_insert = database.check_before_reservation(room_num,from_datetime,until_datetime,first_check=False)
    if bool(check_before_insert) == False:
        reservation_id = database.insert_reservation_info(room_num,name,from_datetime,until_datetime,phone_number,email_address)
    else:
        print(f'We are sorry to inform you that room {room_num} is already reserved by another person for the given time period: {from_datetime} ~ {until_datetime}')
        print(f'Please, choose another time and date and try again.')


def cancel_reservation():
    certain_cancellation = input('Are you sure that you want to cancel the reservation? Yes/No: ').lower()
    if certain_cancellation == 'yes':
        reservation_id = input('Enter your reservation id: ')
        database.insert_cancellation(reservation_id)
    else:
        pass

menu()

