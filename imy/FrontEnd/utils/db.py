import json


class UserSetting:
    def __init__(self, id=0, name="", password="", token=""):
        self.name = name
        self.id = id
        self.password = password
        self.token = token

    def __str__(self):
        return f"{self.name} {self.id}"

    def toJson(self):
        data = {
            "name": self.name,
            "token": self.token,
            "id": self.id,
            "password": self.password,
        }
        return json.dumps(data)

    def toDict(self):
        data = {
            "name": self.name,
            "token": self.token,
            "id": self.id,
            "password": self.password,
        }
        return data

    def fromJson(self, jsonStr):
        data = json.loads(jsonStr)
        self.name = data["name"]
        self.token = data["token"]
        self.id = data["id"]
        self.password = data["password"]

    def fromDict(self, data):
        self.name = data["name"]
        self.token = data["token"]
        self.id = data["id"]
        self.password = data["password"]

    def toFile(self, path="settings.json"):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.toJson())

    def fromFile(self, path=".myenvsettings.json"):
        with open(path, "r", encoding="utf-8") as f:
            self.fromJson(f.read())
