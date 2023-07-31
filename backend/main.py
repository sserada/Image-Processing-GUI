from fastapi import FastAPI, WebSocket, UploadFile, Request
import uvicorn
import json
import os
import base64
from PIL import Image

app = FastAPI()
connected_clients = []

images = {}

@app.websocket('/backend/websocket/{client_id}')
async def upload_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            if (images.get(str(data['name']).split('.')[0]) == None):
                images[str(data['name']).split('.')[0]] = ''
            images[str(data['name']).split('.')[0]] += str(data['data'])
            if data['index'] == data['total']:
                print(str(images[str(data['name']).split('.')[0]]))
                format, image = images[str(data['name']).split('.')[0]].split(',')
                if not os.path.exists('images/' + str(client_id)):
                    os.makedirs('images/' + str(client_id))
                with open('images/' + str(client_id) + '/' + str(data['name']), 'wb') as f:
                    f.write(base64.b64decode(image))
                images[str(data['name']).split('.')[0]] = ''
    except:
        connected_clients.remove(websocket)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

