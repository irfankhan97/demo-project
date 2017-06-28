from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']


print ("Hello! Let\'s get started")

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = input(question)


def add_status():

    updated_status_message = None

    if spy.current_status_message != None:

        print ('Your current status message is %s \n' % (spy.current_status_message))
    else:
        print ('You don\'t have any status message currently \n')

    default = input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print ('%d. %s' % (item_position, message))
            item_position = item_position + 1

        message_selection = int(input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print ('The option you chose is not valid! Press either y or n.')

    if updated_status_message:
        print ('Your updated status message is: %s' % (updated_status_message))
    else:
        print ('You current don\'t have a status update')

    return updated_status_message


def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = input("Please add your friend's name: ")
    new_friend.salutation = input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

   # if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
    friends.append(new_friend)
    print ('Friend Added!')
    #else:
   # print ('Sorry! Invalid entry. We can\'t add spy with the details you provided')

   # return len(friends)


def select_a_friend():
    item_number = 0

    for friend in friends:
        print ('%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating))
        item_number = item_number + 1

    friend_choice = input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():

    friend_choice = select_a_friend()

    original_image = input("What is the name of the image?")
    output_path = "output.jpg"
    text = input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print ("Your secret message image is ready!")


def read_message():

    sender = select_a_friend()

    output_path = input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print ("Your secret message has been saved!")


def read_chat_history():

    read_for = select_a_friend()

    print ('\n6')

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print ('[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message))
        else:
            print ('[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message))


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print ("Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard")

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print ('You have %d friends' % (number_of_friends))
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print ('Sorry you are not of the correct age to be a spy')

if existing.upper() == "Y":
    start_chat(spy)

elif existing.upper() == "N":

    spy = Spy('','',0,0.0)


    spy.name = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = input("Should I call you Mr. or Ms.?: ")

        spy.age = input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print ('Please add a valid spy name')