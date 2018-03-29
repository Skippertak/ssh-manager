#!/usr/bin/python3

import os


# SSH session class
class Session:
    def __init__(self, user, ip, port):
        self.user = user
        self.ip = ip
        self.port = port

    def connect(self):
        os.system('ssh %(0)s@%(1)s -p %(2)s' % {'0': self.user, '1': self.ip, '2': self.port})


test = Session('meg', '192.168.1.32', '22')
test.connect()
