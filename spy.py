from spy_details import spy
from steganography.steganography import Steganography


#FRIENDS LIST
friends = []

#FUNCTIONS USED IN SPYCHAT

#WELCOME NOTE
def print_screen(new_status):
    print("WELCOME " + spy['name'] + " to SPY CHAT\n")
    print("MY STATUS:\n\"" + new_status + "\"\n")
#FOR SELECT FRIEND FUNCTION
def select_friend():
    item_number = 0
    for friend in friends:
        item_number = item_number+1
        print ((item_number),friend['name'])

    friend_choice = input("Choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position
status_messages= []
#ADD STATUS FUNCTION
def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:
        print('Your current status message is %s \n' % (current_status_message))
    else:
        print
        'You don\'t have any status message currently \n'

    default = input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = input("What status message do you want to set? ")
        status_messages.append(new_status_message)
        if len(new_status_message) > 0:

            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in status_messages:
            print( message)
            item_position = item_position + 1

        message_selection = int(input("\nChoose from the above messages "))

        if len(status_messages) >= message_selection:
            updated_status_message = status_messages[message_selection - 1]

    else:
        print
        'The option you chose is not valid! Press either y or n.'

    if current_status_message:
        print
        'Your updated status message is: %s' % (current_status_message)
    else:
        print
        'You current don\'t have a status update'

    return updated_status_message


def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online' : True
    }
    new_friend['name'] = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(new_friend['name']) > 0:
        new_friend['salutation'] = input("Should I call you Mr. or Ms.?: ")

        new_friend['age'] = input("What is your age?")
        new_friend['age'] = int(new_friend['age'])

        new_friend['rating'] = input("What is your spy rating?")
        new_friend['rating'] = float(new_friend['rating'])
        new_friend['is_online'] = True
        friends.append(new_friend)
        return len(friends)





def start_chat():
    spy['name'] = (spy['salutation'] + " " + spy['name'])

    if spy['age'] > 12 and spy['age'] < 50:

        print("Authentication complete. Welcome " + spy['name'] + " , age: " + str(spy['age']) + " , and rating: " + str(spy['rating']) + "-> Proud to have you onboard")


        friends.append(spy)

def menu_chat():
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
        menu_choice = input(menu_choices)

        if len(menu_choice) > 0:

            menu_choice = int(menu_choice)

            if menu_choice == 1:
                print('You chose to update the status')
                new_status = ""
                new_status = add_status(new_status)
                print_screen(new_status)


            else:
                show_menu = False

                if menu_choice == 2:
                    print("You choose to Add Friend")
                    add_friend()
                    menu_chat()
                if menu_choice == 3:
                    print("SELECT FRIEND FROM CONTACTS")
                    select_friend()
                    menu_chat()


    else:
        print
        ('Sorry you are not of the correct age to be a spy')


# WELCOME NOTE
print("WELCOME TO SPY CHAT\n")
print("LET\'S GET STARTED\n")

# USER DETAIL
answer = input("DO U WANT TO CONTINUE AS DEFAULT USER (Y/N)")
if answer.upper() == "Y":
    print("default")
    start_chat()
    menu_chat()
elif answer.upper() == "N":
    print("new user")
    spy['name'] = ''
    spy['salutation'] = ''
    spy['age'] = 0
    spy['rating'] = 0.0
    spy['is_online'] = False

    spy['name'] = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 0:
        spy['salutation'] = input("Should I call you Mr. or Ms.?: ")

        spy['age'] = input("What is your age?")
        spy['age'] = int(spy['age'])

        spy['rating'] = input("What is your spy rating?")
        spy['rating'] = float(spy['rating'])

        spy['is_online'] = True

        start_chat()
        menu_chat()
    else:
        print
        'Please add a valid spy name'
