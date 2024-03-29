﻿# f1_stream_selector
A small web server to get some information about the current/upcoming formula 1  event.
It provides the broadcasting tv station from austria (ORF or ServusTV) to IoT devices and for further usage.

## Data
Currently the data is collected manually. Maybe there is a chance to automate it for the next seasons.
## Docker
The script can run in a docker container.
In this case, the ```Dockerfile```
```Dockerfile
FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir pyyaml pandas

CMD [ "python", "./f1_stream_selector.py" ]
```
should be build with
```sh
docker build -t f1_stream_selector:latest .
```
The recommended way to start the container is with the compose file
```yml
version: "3.9"
services:
  f1_stream_selector:
    image: f1_stream_selector:latest
    container_name: f1_stream_selector
    ports:
        - "8080:8080"
    volumes:
        - /root/f1_stream_selector:/usr/src/app
    restart: unless-stopped
```
Be sure that ```streams.csv```, ```config.yml``` and ```f1_stream_selector.py``` are mounted to ```/usr/src/app``` in the container.

## Config
Use the ```config.yml``` file to set IP and PORT of your webserver.
If the script is running in a docker container, the settings should match the container settings and the port is more or less unimportant for the clients (because of dockers port mapping).

The sample ```config.yml```
```yaml
ip: 0.0.0.0
port: 8080
```
allows the server to listen to any IP on the port 8080.

## Usage
Use
```
http://IP:PORT/stream_now
```
to get the tv station for the weekend.

Use
```
http://IP:PORT/upcoming_country
```
to get the country of the next race.

Use
```
http://IP:PORT/upcoming_circuit
```
to get the name of the next circuit.

Use
```
http://IP:PORT/upcoming_time
```
to get the time until the next race day.

