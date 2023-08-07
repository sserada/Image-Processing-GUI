import os
import json
import base64
import uvicorn
from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post('/api/upload/')
async def image_processing(file: UploadFile = File(...)):
    image_content = await file.read()
    with open('image.jpg', 'wb') as f:
        f.write(image_content)
    encoded_string = base64.b64encode(image_content).decode()
    response = {'processed_image': encoded_string}
    return response

if __name__ == '__main__':
    uvicorn.run(app, host=os.environ['HOST'], port=int(os.environ['PORT']))

