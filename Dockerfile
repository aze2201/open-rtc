FROM alpine:3.18.3

RUN apk update 
RUN apk add python3 py3-pip
RUN pip install flask flask-socketio
RUN mkdir /app
COPY . /app/
WORKDIR /app
ENV FLASK_APP=/app/app.py
ENTRYPOINT flask run --port 8080 --host '0.0.0.0'
