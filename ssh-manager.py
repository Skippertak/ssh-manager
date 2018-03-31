#!/usr/bin/python3

import os


exitWords = ["q", "exit", "quit"]


# SSH session class
class Session:
    def __init__(self, user, ip, port):
        self.user = user
        self.ip = ip
        self.port = port

    def connect(self):
        os.system('ssh %(0)s@%(1)s -p %(2)s' % {'0': self.user, '1': self.ip, '2': self.port})


def display_main():
    os.system('clear')
    print("\t*********************************************************")
    print("\t*****                  SSH Manager!                 *****")
    print("\t*********************************************************")

    try:
        f = open(os.path.expanduser('~/.ssh_manager'), 'r')
        # TODO Read JSON formated list of hosts and print them.
        print("File opened.")
        f.close()
    except FileNotFoundError:
        f = open(os.path.expanduser('~/.ssh_manager'), 'w')
        print("No hosts yet. Consider adding some")
        f.close()


def get_user_choice():
    print("\n\n[1] Add new host.")
    print("[2] Remove old host.")
    print("[q] Quit.")
    choice = input("What would you like to do?")
    display_main()
    if choice == '1':
        print("Placeholder 1")
    elif choice == '2':
        print("Placeholder 2")
    elif choice in exitWords:
        print("Placeholder exit")
    else:
        print("\nNot a valid input")


if __name__ == '__main__':
    display_main()
    while True:
        get_user_choice()
