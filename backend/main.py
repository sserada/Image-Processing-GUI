import asyncio
import base64
import glob
import json
import os

import requests
import uvicorn
import numpy as np
from fastapi import FastAPI, Request, UploadFile, WebSocket
from fastapi.responses import JSONResponse
from PIL import Image
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

app = FastAPI()
connected_clients = {}

images = {}
prediction_results = {}

api_urls = [
        'http://api:8001/api/upload',
        'http://api2:8002/api/upload',
        ]
api_urls = cycle(api_urls)

chunk_size = 1024

async def handle_image(client_id, data, images):
    if images.get(client_id) is None:
        images[client_id] = {}
    if images[client_id].get(str(data['name']).split('.')[0]) is None:
        images[client_id][str(data['name']).split('.')[0]] = ''
    images[client_id][str(data['name']).split('.')[0]] += data['data']
    if data['index'] == data['total']:
        format, image = images[client_id][str(data['name']).split('.')[0]].split(',')
        images[client_id][str(data['name']).split('.')[0]] = ''
        image = base64.b64decode(image)
        await save_image(client_id, data['name'], image, data['image_num'])

async def save_image(client_id, name, image, image_num):
    if not os.path.exists('images/' + str(client_id) + '/unprocessed'):
        os.makedirs('images/' + str(client_id) + '/unprocessed')
    with open('images/' + str(client_id) + '/unprocessed/' + str(name), 'wb') as f:
        f.write(image)
    received_num = len(glob.glob('images/' + str(client_id) + '/unprocessed/*.png')) + len(glob.glob('images/' + str(client_id) + '/unprocessed/*.jpg'))

    if received_num == int(image_num):
        received_data = []

        for image in glob.glob('images/' + str(client_id) + '/unprocessed/*.png') + glob.glob('images/' + str(client_id) + '/unprocessed/*.jpg'):
            received_data.append(image)

        with ThreadPoolExecutor(max_workers=2) as executor:
            for image in received_data:
                api_url = next(api_urls)
                executor.submit(send_api_request, api_url, client_id, image)

        await response_client(client_id)

def send_api_request(api_url, client_id, image):
    with open(image, 'rb') as f:
        file = f.read()
    files = {'file': file}
    response = requests.post(api_url, files=files)
    response = response.json()
    print('Save Request Results')
    if not os.path.exists('images/' + str(client_id) + '/processed'):
        os.makedirs('images/' + str(client_id) + '/processed')
    processed_image = response['processed']
    processed_image = base64.b64decode(processed_image)
    with open('images/' + str(client_id) + '/processed/' + image.split('/')[-1], 'wb') as f:
        f.write(processed_image)

async def response_client(client_id):
    processed_images = glob.glob('images/' + str(client_id) + '/processed/*.png') + glob.glob('images/' + str(client_id) + '/processed/*.jpg')
    for image in processed_images:
        chunks = []
        name = image.split('/')[-1]
        with open(image, 'rb') as f:
            image = f.read()
            image = base64.b64encode(image).decode('utf-8')
        for i in range(0, len(image), chunk_size):
            chunks.append(image[i:i + chunk_size])
        for i in range(len(chunks)):
            data = {'name': name, 'data': chunks[i], 'index': i + 1, 'total': len(chunks)}
            data = json.dumps(data)
            await connected_clients[client_id].send_text(data)
    os.system('rm -rf images/' + str(client_id))
    await connected_clients[client_id].close()

@app.websocket('/backend/websocket/{client_id}')
async def upload_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    connected_clients[client_id] = websocket
    try:
        while True:
            data = await websocket.receive_json()
            await handle_image(client_id, data, images)
    except:
        connected_clients.pop(client_id)
        images.pop(client_id)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

