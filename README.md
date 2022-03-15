# f1_stream_selector
A small web server to get some information about the current/upcoming formula 1  event.
It provides the broadcasting tv station from austria (ORF or ServusTV) to IoT devices or for further usage.

## Data
Currently the data is collected manually. Maybe there is a chance to automate it for the next seasons.
## Config
Use the ```config.yml``` file to set IP and PORT of your webserver.
If the script is running in a docker container, the settings should match the container settings and the port is more or less unimportant for the clients (because of dockers port mapping).

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

