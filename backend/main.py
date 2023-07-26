from fastapi import FastAPI, WebSocket, UploadFile, Request
import uvicorn
import os

app = FastAPI()
connected_clients = []

@app.websocket('/backend/websocket/{client_id}')
async def upload_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            print(data)
    except:
        connected_clients.remove(websocket)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

