#!/usr/bin/python3

import os


# Functions

def display_main():
    os.system('clear')
    print("\t*********************************************************")
    print("\t*****                  SSH Manager!                 *****")
    print("\t*********************************************************")

    try:
        f = open(os.path.expanduser('~/.ssh_manager'), 'r')
        # TODO Read JSON formated list of hosts and print them.
        f.close()
    except FileNotFoundError:
        f = open(os.path.expanduser('~/.ssh_manager'), 'w')
        print("No hosts yet. Consider adding some")
        f.close()

def get_user_choice():
    print("\n\n[1] Add new host.")
    print("[2] Remove old host.")
    print("[q] Quit.")

    return input("What would you like to do?")

def host_status():
    # TODO Is the host up or down?
    return

def add_host():
    # TODO Add hosts with JSON layout
    file = open(os.path.expanduser('~/.ssh_manager'), 'a')
    print("File opened")
    file.close()

def remove_host():
    # TODO Remove a host you decide
    print("Placeholder remove host")

def connect_to_host():
    # TODO SSH in. With optional arguments like reverse proxy.
    return

def quit():
    # TODO Find a use for an exit function
    print("Placeholder quit")


# Variables and init

choice = ''
exitWords = ["q", "exit", "quit"]
display_main()

# Main loop

while choice not in exitWords:

    choice = get_user_choice()
    display_main()

    if choice == '1':
        add_host()
    elif choice == '2':
        remove_host()
    elif choice in exitWords:
        quit()
    else:
        print("\nNot a valid input")
