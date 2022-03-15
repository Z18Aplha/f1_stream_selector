# f1_stream_selector
A small web server to push todays formula 1 tv station from austria (ORF or ServusTV) to IoT devices or for further usage.

## Data
Currently the data is collected manually. Maybe there is a chance to automate it for the next seasons.
## Config
Use the ```config.yml``` file to set IP and PORT of your webserver.
If the script is running in a docker container, the settings should match the container settings and the port is more or less unimportant for the clients (because of dockers port mapping).

## Usage
Use
```
http://IP:PORT/stream_today
```
to get todays tv station.

Use
```
http://IP:PORT/country_today
```
to get todays country.

Use
```
http://IP:PORT/circuit_today
```
to get the name of todays circuit.

