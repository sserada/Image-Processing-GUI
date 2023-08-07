import os
import glob
import json
import base64
import asyncio
import uvicorn
import requests
from PIL import Image
from fastapi import FastAPI, WebSocket, UploadFile, Request, BackgroundTasks

app = FastAPI()
connected_clients = []

images = {}
image_num = {}

def handle_image(client_id, data, images):
    if (images.get(str(data['name']).split('.')[0]) == None):
        images[str(data['name']).split('.')[0]] = ''
    images[str(data['name']).split('.')[0]] += str(data['data'])
    if data['index'] == data['total']:
        image_num[str(client_id)] = image_num.get(str(client_id), 0) + 1
        print(image_num[str(client_id)])
        format, image = images[str(data['name']).split('.')[0]].split(',')
        image = base64.b64decode(image)
        save_image(client_id, data['name'], image)
        send_api_request(client_id, data['name'], image)

def save_image(client_id, name, image):
    if not os.path.exists('images/' + str(client_id)):
        os.makedirs('images/' + str(client_id))
    with open('images/' + str(client_id) + '/' + str(name), 'wb') as f:
        f.write(image)

def send_api_request(client_id, name, image):
    files = {'file': image}
    response = requests.post('http://api:8001/api/upload', files=files)
    response = response.json()
    processed_image = response['processed_image']
    print(processed_image)
    processed_image = base64.b64decode(processed_image)
    with open('images/' + str(client_id) + '/processed_' + str(name), 'wb') as f:
        f.write(processed_image)

@app.websocket('/backend/websocket/{client_id}')
async def upload_endpoint(websocket: WebSocket, client_id: str, background_task: BackgroundTasks):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            handle_image(client_id, data, images)
    except:
        connected_clients.remove(websocket)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

