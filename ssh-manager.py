#!/usr/bin/python3

import os

## Debug test data
data = {'IP': [],
        'port': []}


## Main class
class Manager:
    def __init__(self, user, ip, port):
        self.user = ""
        self.ip = ""
        self.port = "22"

    def connect(self):
        os.system('ssh %(0)s@%(1)s -p %(2)s' % {'0': self.user, '1': self.ip, '2': self.port}')

session = Manager('meg', '192.168.1.32', '22')
session.connect()