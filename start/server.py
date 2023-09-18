import asyncio
import time

from websockets.server import serve


def handle_msg(msg):
    return f"Update message: {msg} at time {time.time()}"


async def echo(websocket):
    async for msg in websocket:
        await websocket.send(handle_msg(msg))


async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
