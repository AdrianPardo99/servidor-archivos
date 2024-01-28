FROM python:latest


RUN mkdir /app
WORKDIR /app

ARG BUILD_ENVIRONMENT=base

# Installing apps
RUN apt-get update && apt-get install -y postgresql netcat-traditional 

# Install dependencies:
COPY ./requirements .

RUN pip install -r ${BUILD_ENVIRONMENT}.txt

COPY . .


COPY wait.sh /wait.sh
RUN sed -i 's/\r$//g' /wait.sh
RUN chmod +x /wait.sh

COPY start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
