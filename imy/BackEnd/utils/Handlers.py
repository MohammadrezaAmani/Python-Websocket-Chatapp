from imy.BackEnd.utils.hasing import send
from imy import UsersDB, MessagesDB


async def StartHandler(websocket, data: dict):
    user = UsersDB.add(data["name"], data["password"], websocket)
    UsersDB.save()
    await send(websocket, user.toJson())


async def MessageHandler(data: dict):
    MessagesDB.addFromDict(data)
    await send(UsersDB.getWebSocket(data["toUser"]), data)


async def All_UsersHandler(websocket):
    await send(websocket, UsersDB.getAllJson())


async def LoginHandler(websocket, data: dict):
    user = UsersDB.searchByName(data["name"])
    if user == None:
        await send(websocket, {"type": "ERROR", "message": "User not found"})
        return
    if user.password != data["password"]:
        await send(websocket, {"type": "ERROR", "message": "Wrong password"})
        return
    UsersDB.updateWebSocket(user, websocket)
    await send(websocket, user.toJson())
