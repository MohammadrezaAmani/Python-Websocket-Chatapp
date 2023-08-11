import asyncio
from websockets.server import serve
from imy.models.models import Types
from imy import config
from .utils.hasing import recive
from .utils.Handlers import StartHandler, MessageHandler, All_UsersHandler, LoginHandler


async def Handler(websocket):
    async for message in websocket:
        data = recive(message)
        print(data, type(data))
        if data["type"] == Types.START:
            await StartHandler(websocket, data)

        elif data["type"] == Types.MESSAGE:
            await MessageHandler(data)

        elif data["type"] == Types.CLOSE:
            await websocket.close()
            break

        elif data["type"] == Types.ALL_USERS:
            await All_UsersHandler(websocket)

        elif data["type"] == Types.LOGIN:
            await LoginHandler(websocket, data)


async def backend():
    async with serve(Handler, config.IP, config.PORT):
        await asyncio.Future()
