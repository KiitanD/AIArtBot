# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install zip -y
# RUN pip install kaggle
COPY . .
COPY ./kaggle.json ./root/.kaggle/kaggle.json
COPY ./kaggle.json ./.kaggle/kaggle.json
COPY ./testy.sh ./testy.sh
RUN chmod +x ./testy.sh
CMD ls -a ./root/.kaggle
COPY ./kernelrun.sh ./kernelrun.sh
RUN chmod +x ./kernelrun.sh
CMD ./kernelrun.sh

#need to copy all files from sources into docker container