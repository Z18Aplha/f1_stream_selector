import pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import yaml
from datetime import datetime


def get_df():
    df = pd.read_csv("streams.csv", index_col="Date", parse_dates=True, dayfirst=True)
    df.index = df.index.date
    df = df.sort_index()
    df = df[~df.index.duplicated(keep='last')]
    return df


def get_stream_now(df=None):
    if df is None:
        df = get_df()

    stream = df[df.index == datetime.now().date()]["Stream"]
    if not len(stream):
        stream = "NOSTREAM"
    else:
        stream = stream[0]
    
    return stream
    
def get_country_upcoming(df=None):
    if df is None:
        df = get_df()
    try:
        country = df[df.index >= datetime.now().date()].iloc[0]["Country"]
    except KeyError:
        country = "NOCOUNTRY"
    return country

def get_circuit_upcoming(df=None):
    if df is None:
        df = get_df()
    try:
        circuit = df[df.index >= datetime.now().date()].iloc[0]["Circuit"]
    except:
        circuit = "NOCIRCUIT"
    return circuit

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>F1 Stream Selector</title></head>", "utf-8"))
        if self.path == "/stream_now":
            stream = get_stream_now()
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes(f"<p>{stream}</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif self.path == "/country_upcoming":
            country = get_country_upcoming()
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes(f"<p>{country}</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif self.path == "/circuit_upcoming":
            circuit = get_circuit_upcoming()
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes(f"<p>{circuit}</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes(f"<p>ERROR</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    # load config
    with open("config.yml", "r") as stream:
        try:
            cfg = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    hostName = cfg["ip"]
    serverPort = cfg["port"]

    # server stuff
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
