import re
from datetime import datetime as dt


def __room_info(return_type=None) -> str:
    """
    This function ensures that a user's "room number" input is not null and is in the correct format.,
    :param return_type: If this function is used by the 'check_reservation()' function, then return_type should be equal to "check," but if it is used for the 'make_reservation()' function, then return_type should be equal to "None."
    :return string value
    """
    room_num = None
    while type(room_num) != int:
        try:
            if return_type == 'check':
                room_num = int(input('Which room are you interested in?: '))
            else:
                room_num = int(input('Enter the room number that you want to reserve: '))
            if room_num not in (1, 2, 3, 4, 5):
                if return_type == 'check':
                    print(f"The room {room_num} does not exist. Please, enter an existing room number.")
                else:
                    print(f"Please make a valid selection. The room {room_num} does not exist.")
                room_num = None
        except ValueError:
            print("Invalid input. Please, try again")
    return str(room_num)


def __from_date_info(return_type=None) -> str:
    """
    This function ensures that a user's "from-date" input is not null, is not out of range for the month, and is in the correct format.,
    :param return_type: If this function is used by the 'check_reservation()' function, then return_type should be equal to "check," but if it is used for the 'make_reservation()' function, then return_type should be equal to "None.",
    :return string value
    """
    match_from = None
    while bool(match_from) != True:
        try:
            if return_type == 'check':  # For checking reservations
                print("Enter in the following format 'YYYY-MM-DD' from what date you want to check the reservations.")
                from_date = input('From:')
                pattern = r'\d{4}-\d?\d-\d\d$'
            else:  # For making reservations
                from_date = input('Enter in the following format YYYY-MM-DD HH:MM the exact date and time from when you want to reserve the room: ')
                pattern = r'\d{4}-\d?\d-\d?\d (?:2[0-3]|[01]?[0-9]):[0-5]?[0-9]{2}$'
            match_from = re.match(pattern, string=from_date)
            if len(from_date) == 0:
                if return_type == 'check':
                    print('You did not enter from what date and time you would like to check reservations.')
                else:
                    print('You have not entered from when and what time you need the room.')
                match_from = None
            elif bool(match_from) == False:
                if return_type == 'check':
                    print(f"You entered the date, not in the correct format.")
                else:
                    print(f"You entered the date and time, not in the correct format.")
                    match_from = None
            if return_type == 'check':
                dt.strptime(from_date, '%Y-%m-%d')
            else:
                dt.strptime(from_date, '%Y-%m-%d %H:%M')
        except ValueError:
            print("Invalid input. Please try again: ")
            match_from = None

    return from_date


def __until_date_info(from_datetime, return_type=None) -> str:
    """
    This function ensures that a user's until-date input is not null, it is not out of range for the month, and it is in the correct format.,
    :param return_type: If this function is used by the 'check_reservation()' function, then return_type should be equal to "check," but if it is used for the 'make_reservation()' function, then return_type should be equal to "None."
    :param from_datetime: The "from-date" value is needed for comparing it to the 'until-date' value to ensure the "End Date" is not less than the "Start Date.",
    :return string value
    """
    later_then_start = False
    while later_then_start != True:
        try:
            match_until = None
            while bool(match_until) != True:
                try:
                    if return_type == 'check':  # For checking reservations
                        print("Enter in the following format 'YYYY-MM-DD' until what date you want to check the reservations.")
                        until_date = input('Until:')
                        pattern = r'\d{4}-\d?\d-\d\d$'

                    else:  # For making reservations
                        until_date = input("Enter in the following format 'YYYY-MM-DD HH:MM' the exact date and time until when you want to reserve the room: ")
                        pattern = r'\d{4}-\d?\d-\d?\d (?:2[0-3]|[01]?[0-9]):[0-5]?[0-9]{2}$'

                    match_until = re.match(pattern, string=until_date)

                    if len(until_date) == 0:  # For checking reservations
                        if return_type == 'check':
                            print('You did not enter until what date you would like to check reservations.')
                        else:  # For making reservations
                            print('You did not enter until when and at what time you need the room.')
                        match_until = None

                    elif bool(match_until) == False:
                        if return_type == 'check':
                            print(f"You entered the date, not in the correct format.")
                        else:
                            print(f"You entered the date and time, not in the correct format.")
                            match_until = None

                except ValueError:
                    print("Invalid input. Please try again: ")
            if return_type == 'check':
                later_then_start = dt.strptime(from_datetime, '%Y-%m-%d') < dt.strptime(until_date, '%Y-%m-%d')
            else:
                later_then_start = dt.strptime(from_datetime, '%Y-%m-%d %H:%M') < dt.strptime(until_date, '%Y-%m-%d %H:%M')
            if later_then_start == True:
                return until_date
            else:
                print("Invalid input. The 'End Date' cannot be less than the 'Start Date.' Please, check your input and try again.")
        except ValueError:
            print('The day is out of range for the month. Please check how many days in the entered month and try again.')
            continue


def __phone_number_info() -> str:
    """
    This function ensures that a user's "phone number" input is not null and is in the correct format.,
    :return string value
    """
    match_phone = None
    while bool(match_phone) != True:
        try:
            phone_number = input('Enter your phone number in the following format +992 XXX XXX XXX: ')
            pattern = r'\d{9}$'
            match_phone = re.match(pattern, string=phone_number)
            if len(phone_number) == 0:
                print('You did not enter your phone number.')
                match_until = None
            elif bool(match_phone) == False:
                print(f"You entered your phone number, not in the correct format.")
                match_phone = None
        except ValueError:
            print("Invalid input. Please try again: ")
    return phone_number


def __email_address_info() -> str:
    """
    This function ensures that a user's "phone number" input is not null and is in the correct format.,
    :return string value
    """
    match_email = None
    while bool(match_email) != True:
        try:
            email_address = input('Enter your email address example@gmail.com: ')
            pattern = r'\w+[@]\w+[.]\w+'
            match_email = re.match(pattern, string=email_address)
            if len(email_address) == 0:
                print('You did not enter your email address.')
                match_email = None
            elif bool(match_email) == False:
                print(f'Invalid email address. Please check and re-enter your email address')
                match_email = None
        except ValueError:
            print('Invalid input. Please try again: ')
    return email_address

