USER_CHOICE = """
Enter:
 '1' to check reservation for specific time of the room
 '2' to make a reservation
 '3' cancel reservation
'q' to quit
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
    specific_room = input('Are you interested in a specific room? Yes/No')
    if specific_room == 'Yes':
        room_num = input('Which room are you interested in: ')
        print("Enter in the following format 'YYYY-MM-DD' from what date you want to check the reservations.")
        date_from = input('From:')
        print("Enter in the following format 'YYYY-MM-DD' until what date you want to check the reservations.")
        date_until = input('Until:')
    else:
        print("Enter in the following format 'YYYY-MM-DD HH:MM' from what date you want to check the reservations.")
        date_from = input('From:')
        print("Enter in the following format 'YYYY-MM-DD HH:MM' until what date you want to check the reservations.")
        date_until = input('Until:')




def make_reservation():

    room_num = None
    while type(room_num) != int:
        try:
            room_num = int(input('Enter room number that you want to reserve: '))
            if room_num not in (1, 2, 3, 4, 5):
                print(f"Please make a valid selection. The room {room_num} does not exist.")
                room_num = None
        except ValueError:
            print("Please enter a number, not alphanumeric.")

    name = str(input('Enter your name: '))
    from_datetime = input("Enter in the following format 'YYYY-MM-DD' HH:MM the exact date and time from when you want to reserve the room: ")
    until_datetime = input("Enter in the following format 'YYYY-MM-DD HH:MM'  the exact date and time until when you want to reserve the room")
    phone_number = input('Enter your phone number in the following format +992 XXX XXX XXX: ')
    email_address = input('Enter your email address: ')



def cancel_reservation():
    phone_num = input('Enter your phone number: ')
    date = input('Enter the date and time: ')


menu()