#!/usr/bin/python3

import os
import sys
import json
import time


exitWords = ["q", "exit", "quit"]


def init():
    try:
        with open(os.path.expanduser('~/.ssh_manager'), mode='r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        with open(os.path.expanduser('~/.ssh_manager'), mode='w', encoding='utf-8') as f:
            json.dump([], f)
            print("~/.ssh_manager created. It will be used to store hosts data.")
            time.sleep(2)
    display_main()


def connect(user, ip, port=22):
    os.system('ssh %(0)s@%(1)s -p %(2)s' % {'0': user, '1': ip, '2': port})


def display_main():
    os.system('clear')
    print("\t*********************************************************")
    print("\t*****                  SSH Manager!                 *****")
    print("\t*********************************************************")
    print("\n\n[1] Add new host.")
    print("[2] Remove old host.")
    print("[3] Connect to an IP.")
    print("[q] Quit.")


def display_hosts():
    with open(os.path.expanduser('~/.ssh_manager'), mode='r', encoding='utf-8') as f:
        json_data = json.load(f)
        print(json_data)


def display_add_host():
    os.system('clear')
    print("\t*********************************************************")
    print("\t*****                  SSH Manager!                 *****")
    print("\t*********************************************************")
    print("Placeholder add host")


def display_remove_hosts():
    os.system('clear')
    print("\t*********************************************************")
    print("\t*****                  SSH Manager!                 *****")
    print("\t*********************************************************")
    print("Placeholder remove host")


def display_ssh_ip():
    os.system('clear')
    print("\t*********************************************************")
    print("\t*****                  SSH Manager!                 *****")
    print("\t*********************************************************")
    ssh_name = input("\nWhat user do you want to ssh in as? ")
    ssh_ip = input("\nWhat IP do you want to SSH in to? ")
    connect(ssh_name, ssh_ip)
    display_main()


def get_user_choice():
    choice = input("\nWhat would you like to do?\n")
    if choice == '1':
        display_remove_hosts()
    elif choice == '2':
        display_remove_hosts()
    elif choice == '3':
        display_ssh_ip()
    elif choice in exitWords:
        sys.exit()
    else:
        print("\nNot a valid input")


if __name__ == '__main__':
    init()
    while True:
        get_user_choice()
