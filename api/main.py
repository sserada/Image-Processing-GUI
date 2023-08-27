import os
import cv2
import json
import base64
import uvicorn
from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse

app = FastAPI()
image_path = 'images/' + os.environ['PORT'] + '.jpg'

@app.on_event("startup")
async def startup_event():
    # You can load neural networks, etc. here.
    if not os.path.exists('images'):
        os.makedirs('images')

@app.post('/api/upload')
async def image_processing(file: UploadFile = File(...)):
    image_content = await file.read()
    print('Received image')
    with open(image_path, 'wb') as f:
        f.write(image_content)

    # Write the code to process the image here.
    # For example, read the image using OpenCV and convert it to grayscale.
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(image_path, gray)
    with open(image_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    os.remove(image_path)
    response = {'processed': encoded_string}
    return response

if __name__ == '__main__':
    uvicorn.run(app, host=os.environ['HOST'], port=int(os.environ['PORT']))

