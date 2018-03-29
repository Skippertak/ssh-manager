#!/usr/bin/python3
# Test
import os, json

import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

## Debug data test
data =  {'IP': [],
         'port': []}

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
"""
def add_host():
    # TODO Add hosts with JSON layout
    file = open(os.path.expanduser('~/.ssh_manager'), 'a')
    print("File opened")
    file.close()
"""
def add_host():
    # Write JSON file
    with io.open(os.path.expanduser('~/.ssh_manager'), 'w', encoding='utf8') as outfile:
        data[1] = int(input("Whats the IP?"))
        data[2] = int(input("Whats the port?"))
        int_ = json.dumps(data,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(int_))

    # Read JSON file
    with open(os.path.expanduser('~/.ssh_manager')) as data_file:
        data_loaded = json.load(data_file)

    print(data == data_loaded)

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
