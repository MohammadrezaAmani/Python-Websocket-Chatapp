from websockets.sync.client import connect
import random
from threading import Thread
from imy.models.models import Message, User, Command
from imy.FrontEnd.utils.db import UserSetting
from imy import config
import json
import os
from imy.BackEnd.utils.db import Messages


class FrontEnd:
    def __init__(self):
        self.messages = Messages()

    def createConnection(self):
        self.websocket = connect(
            f"ws://{config.IP}:{config.PORT}", open_timeout=100, close_timeout=100)

    def SignUp(self, name, password):
        self.websocket.send(Command.START(name, password))
        message = json.loads(self.websocket.recv())
        if message["type"] == "error":
            return False
        self.me = UserSetting()
        self.me.fromDict(message)
        self.me.toFile(path=config.SETTiNGS_PATH)
        return True

    def Login(self, name, password):
        self.websocket.send(Command.LOGIN(name, password))
        message = json.loads(self.websocket.recv())
        if message["type"] == "error":
            return False
        self.me = UserSetting()
        self.me.fromDict(message)
        self.me.toFile(path=config.SETTiNGS_PATH)
        return True

    def send(self, data):
        self.websocket.send(json.dumps(data))

    def sendMessage(self, toUser, message):
        m = Message(random.randint(0, 100), self.me.id,
                    int(toUser), message).toDict()
        self.send(m)

    def recive(self):
        while True:
            if self.websocket.recv_events:
                data = self.websocket.recv()
                # self.data = json.loads(data)
                # if data['type'] == 'error':
                #     self.error = data['error']

                # if data['type'] == 'message':
                #     self.messages.addFromDict(data)

                # if data['type'] == 'all_users':
                #     self.all_users = data['users']
                print(data)

    def CLI(self):
        firstText = """
welcome!
1- login.
2- sign up.
3- exit.
        """
        while True:
            os.system("clear")
            print(firstText)
            command = input("command: ")
            if command == "1":
                os.system("clear")
                print("login menu: ")
                name = input("name: ")
                password = input("password: ")
                if self.Login(name, password):
                    break
                else:
                    print("wrong username or password")
                input("press enter to continue")
            elif command == "2":
                os.system("clear")
                print("sign up menu: ")
                name = input("name: ")
                password = input("password: ")
                if self.SignUp(name, password):
                    break
                else:
                    print("username already exists")
                input("press enter to continue")
            elif command == "3":
                exit()
            else:
                print("wrong command")

    def HomeCLI(self):
        text = """
Welcome dear %s, Inter your choice:
1- send message.
2- list of users.
3- list of messages.
4- exit.
        """
        while True:
            os.system("clear")
            print(text % self.me.name)
            command = input("command: ")
            if command == "1":
                toUser = input("to user: ")
                message = input("message: ")
                self.sendMessage(toUser, message)
                input("press enter to continue")
            elif command == "2":
                os.system("clear")
                print("send message menu: ")
                m = Command.ALL_USERS()
                self.send(m)
                input("press enter to continue")
            elif command == "3":
                os.system("clear")
                print(text % self.me.name)
                print(self.messages)
                input("press enter to continue")
            elif command == "4":
                exit()
            else:
                print("wrong command")

    def reciveThread(self):
        self.thread = Thread(target=(self.recive))
        self.thread.start()


def frontend():
    fe = FrontEnd()
    fe.createConnection()
    fe.CLI()
    fe.reciveThread()
    fe.HomeCLI()
