import json


async def send(websocket, message):
    if type(message) == dict:
        await websocket.send(json.dumps(message))
    else:
        await websocket.send(message)


def recive(message):
    return json.loads(message)


def createToken(user):
    data = user.name * 2 + user.password * 2
    data = data.encode("utf-8")
    data = data.hex()
    data = {
        "type": "token",
        "token": data,
    }
    return json.dumps(data, indent=4)
