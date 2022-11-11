from utils import UserInputHandler

USER_CHOICE = """
Enter:
 '1' to check reservation of a specific room or all rooms.
 '2' to make a reservation.
 '3' cancel reservation.
 'q' to quit.
Your choice: """


def menu():

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

    else:
        from_date = UserInputHandler.__from_date_info(return_type='check')
        until_date = UserInputHandler.__until_date_info(from_datetime = from_date,return_type ='check')
        


def make_reservation():

    #Room information
    room_num = UserInputHandler.__room_info()

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


def cancel_reservation():
    certain_cancellation = input('Are you sure that you want to cancel the reservation? Yes/No: ').lower()
    if certain_cancellation == 'yes':
        reservation_id = input('Enter your reservation id: ')
    else:
        pass

menu()

