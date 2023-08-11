import json
import datetime


class Types:
    COMMAND = "COMMAND"
    MESSAGE = "MESSAGE"
    START = "START"
    CLOSE = "CLOSE"
    ALL_USERS = "ALL_USERS"
    USER = "USER"
    LOGIN = "LOGIN"
    SIGNUP = "SIGNUP"
    LOGOUT = "LOGOUT"


class User:
    def __init__(self, id=1, name="me", password="1234", token="1234"):
        self.name = name
        self.id = id
        self.password = password
        self.token = token

    def __str__(self):
        return f"{self.name} {self.id}"

    def toJson(self):
        data = {
            "name": self.name,
            "id": self.id,
            "password": self.password,
            "token": self.token,
            "type": Types.USER,
        }
        return data

    def toDict(self):
        data = {
            "name": self.name,
            "id": self.id,
            "password": self.password,
            "token": self.token,
            "type": Types.USER,
        }
        return data

    def toJsonSecure(self):
        data = {
            "name": self.name,
            "id": self.id,
            "token": self.token,
            "type": Types.USER,
        }
        return data

    def fromJson(self, jsonStr):
        data = json.loads(str(jsonStr))
        self.name = data["name"]
        self.id = data["id"]
        self.password = data["password"]
        self.token = data["token"]

    def fromDict(self, data):
        self.name = data["name"]
        self.id = data["id"]
        self.password = data["password"]
        self.token = data["token"]

    def isAuth(self):
        return self.token != None


class Message:
    def __init__(
        self,
        id=0,
        fromUser=0,
        toUser=0,
        message="EmptyMessage",
        sendTime=datetime.datetime.now(),
        isResived=False,
    ):
        self.id = id
        self.fromUser = fromUser
        self.toUser = toUser
        self.message = message
        self.sendTime = str(sendTime)
        self.isResived = isResived

    def __str__(self):
        data = {
            "id": self.id,
            "fromUser": self.fromUser,
            "toUser": self.toUser,
            "message": self.message,
            "sendTime": self.sendTime,
            "isResived": self.isResived,
            "type": Types.MESSAGE,
        }
        return str(json.dumps(data, indent=4))

    def toJson(self):
        data = {
            "id": self.id,
            "fromUser": self.fromUser,
            "toUser": self.toUser,
            "message": self.message,
            "sendTime": self.sendTime,
            "isResived": self.isResived,
            "type": Types.MESSAGE,
        }
        return data

    def toDict(self):
        data = {
            "id": self.id,
            "fromUser": self.fromUser,
            "toUser": self.toUser,
            "message": self.message,
            "sendTime": self.sendTime,
            "isResived": self.isResived,
            "type": Types.MESSAGE,
        }
        return data

    #! has known bug, use fromDict instead

    def fromJson(self, jsonStr):
        data = json.loads(str(jsonStr))
        self.id = data["id"]
        self.fromUser = data["fromUser"]
        self.toUser = data["toUser"]
        self.message = data["message"]
        self.sendTime = data["sendTime"]
        self.isResived = data["isResived"]

    def fromDict(self, data):
        self.id = data["id"]
        self.fromUser = data["fromUser"]
        self.toUser = data["toUser"]
        self.message = data["message"]
        self.sendTime = data["sendTime"]
        self.isResived = data["isResived"]


class Command:
    def START(name, password):
        data = {"type": Types.START, "password": password, "name": name}
        return json.dumps(data, indent=4)

    def ALL_USERS():
        data = {"type": Types.ALL_USERS}
        return data

    def LOGIN(name, password):
        data = {
            "type": Types.LOGIN,
            "name": name,
            "password": password,
        }
        return json.dumps(data, indent=4)


class Errors:
    ALREADY_LOGGED_IN = "1: ALREADY_LOGGED_IN"
    ALREADY_EXISTS = "2: ALREADY_EXISTS"
    NOT_FOUND = "3: NOT_FOUND"
    WRONG_PASSWORD = "4: WRONG_PASSWORD"
    NOT_AUTH = "5: NOT_AUTH"
    NOT_LOGGED_IN = "6: NOT_LOGGED_IN"
    NOT_ALLOWED = "7: NOT_ALLOWED"
    NOT_VALID = "8: NOT_VALID"
    NOT_CONNECTED = "9: NOT_CONNECTED"
    NOT_CONNECTED_TO_USER = "10: NOT_CONNECTED_TO_USER"
    NOT_CONNECTED_TO_SERVER = "11: NOT_CONNECTED_TO_SERVER"
    WRONG_FORMAT = "12: WRONG_FORMAT"
    UNKNOWN = "13: UNKNOWN"

    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        return self.message

    class toJson:
        def __init__(self, message=""):
            self.message = message

        def __str__(self):
            return json.dumps({"error": self.message})
