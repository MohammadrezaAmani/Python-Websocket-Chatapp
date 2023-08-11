from imy.models.models import User, Message, Errors
from imy.BackEnd.utils.hasing import createToken
from imy import config
import json
import os


class Users:
    def __init__(self):
        self.users = {}

    def add(self, name, password, websocket):
        if self.searchByName(name) != None:
            return Errors.toJson(Errors.ALREADY_EXISTS)
        user = User(
            name=name,
            password=password,
            id=len(self.users) + 1,
            token=createToken(User(name=name, password=password)),
        )
        self.users[len(self.users) + 1] = {"USER": user, "WEBSOCKET": websocket}
        return user

    def get(self, id):
        try:
            return self.users[id]
        except:
            return Errors.toJson(Errors.NOT_FOUND)

    def getWebSocket(self, id):
        return self.users[id]["WEBSOCKET"]

    def getAll(self):
        try:
            return self.users
        except:
            return Errors.toJson(Errors.NOT_FOUND)

    def getAllJson(self):
        users = {}
        for user in self.users:
            users[user] = self.users[user]["USER"].toDict()
        return users

    def save(self, path=config.DB_PATH):
        try:
            with open(path, "w") as f:
                f.write(str(json.dumps(self.getAllJson(), indent=4)))
        except Exception as e:
            print(e)

    def load(self, path=config.DB_PATH):
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    users = json.loads(f.read())
                    for user in users:
                        print(users, type(user), type(users))
                        print(user)
                        if self.searchByName(users[user]["name"]) != None:
                            continue
                        self.users[user] = {
                            "USER": User.fromJson(users[user]),
                            "WEBSOCKET": None,
                        }
            except Exception as e:
                print(e)

    def remove(self, id):
        try:
            del self.users[id]
        except:
            return Errors.toJson(Errors.NOT_FOUND)

    def __len__(self):
        return len(self.users)

    def __str__(self):
        return str(self.users)

    # +
    def __getitem__(self, id):
        return self.get(id)

    def login(self, name, password, websocket):
        for user in self.users:
            if self.users[user]["USER"].name == name:
                if self.users[user]["USER"].password == password:
                    self.users[user]["WEBSOCKET"] = websocket
                    return self.users[user]["USER"]
                else:
                    return Errors.toJson(Errors.WRONG_PASSWORD)
        return Errors.toJson(Errors.NOT_FOUND)

    def searchByName(self, name):
        for user in self.users:
            if self.users[user]["USER"].name == name:
                return self.users[user]["USER"]
        return None

    def searchByID(self, id):
        for user in self.users:
            if self.users[user]["USER"].id == id:
                return self.users[user]["USER"]
        return None

    def searchByToken(self, token):
        for user in self.users:
            if self.users[user]["USER"].token == token:
                return self.users[user]["USER"]
        return None

    def updateWebSocket(self, user, websocket):
        for u in self.users:
            if self.users[u]["USER"].id == user.id:
                self.users[u]["WEBSOCKET"] = websocket
                return True
        return False


class Messages:
    def __init__(self):
        self.messages = {}

    def add(self, message: Message):
        self.messages[len(self.messages) + 1] = message

    #! has known bug, use addFromDict instead
    def addFromJson(self, jsonStr):
        m = Message()
        m.fromJson(jsonStr)
        self.messages[len(self.messages) + 1] = m

    def addFromDict(self, data):
        m = Message()
        m.fromDict(data)
        self.messages[len(self.messages) + 1] = m

    def get(self, id):
        return self.messages[id]

    def getAll(self):
        return self.messages

    def remove(self, id):
        del self.messages[id]

    def __len__(self):
        return len(self.messages)

    def __str__(self):
        return str(self.messages)

    # +
    def __getitem__(self, id):
        return self.messages[id]

    def searchByID(self, id):
        for message in self.messages:
            if self.messages[message].id == id:
                return self.messages[message]
        return None

    def searchByFromUser(self, id):
        for message in self.messages:
            if self.messages[message].fromUser == id:
                return self.messages[message]
        return None

    def searchByToUser(self, id):
        for message in self.messages:
            if self.messages[message].toUser == id:
                return self.messages[message]
        return None

    def searchByText(self, text):
        for message in self.messages:
            if text in self.messages[message].message:
                return self.messages[message]
        return None
