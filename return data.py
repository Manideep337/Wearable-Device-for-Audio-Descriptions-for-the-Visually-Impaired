import websockets
import os
import asyncio

async def send_file(websocket, filename):
    with open(filename, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            await websocket.send(data)


async def main():
    async with websockets.serve(send_file, "localhost", 8765):
        await asyncio.Future()  # wait forever


if __name__ == "__main__":
    asyncio.run(main())
