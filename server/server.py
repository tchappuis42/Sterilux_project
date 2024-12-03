import asyncio
import websockets
import json

def process_coordinates(data):
	x = data.get("x")
	y = data.get("y")
	sw = data.get("sw")
	sh = data.get("sh")
	#print(f"Reçu : x={x}, y={y}")
	#print(f"Reçu : sw={sw}, sh={sh}")
	if x < sw / 2 and y < sh / 2:
		print("top left")
	elif x < sw / 2 and y > sh / 2:
		print("bottom left")
	elif x > sw / 2 and y > sh / 2:
		print("bottom right")
	else:
		print("top right")


async def handle_connection(websocket):
	print("Client connecté !")
	try:
		async for message in websocket:
			data = json.loads(message)
			process_coordinates(data)
			
	except websockets.exceptions.ConnectionClosed:
		print("Client déconnecté.")

async def main():
    print("Serveur WebSocket démarré sur ws://127.0.0.1:9000")
    async with websockets.serve(handle_connection, "127.0.0.1", 9000):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())