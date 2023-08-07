FROM python:3.10.0

WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8001

