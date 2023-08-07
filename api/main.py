import os
import cv2
import json
import base64
import uvicorn
from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post('/api/upload/')
async def image_processing(file: UploadFile = File(...)):
    image_content = await file.read()
    print('Received image')
    with open('image.jpg', 'wb') as f:
        f.write(image_content)

    # Write the code to process the image here.
    # For example, read the image using OpenCV and convert it to grayscale.
    img = cv2.imread('image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('image.jpg', gray)
    with open('image.jpg', 'rb') as f:
        encoded_string = base64.b64encode(f.read()).decode()
        print(encoded_string)

    response = {'processed_image': encoded_string}
    return response

if __name__ == '__main__':
    uvicorn.run(app, host=os.environ['HOST'], port=int(os.environ['PORT']))

