import pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import yaml


def get_stream_today():
    # load csv
    df = pd.read_csv("streams.csv", index_col="Date",
                     parse_dates=True, dayfirst=True)
    df.index = pd.to_datetime(df.index)
    # find exact date in df
    try:
        stream = df.loc[pd.to_datetime('today').normalize().date().isoformat()]["Stream"]
        return stream
    except KeyError:
        return "NOSTREAM"
    
def get_country_today():
    # load csv
    df = pd.read_csv("streams.csv", index_col="Date",
                     parse_dates=True, dayfirst=True)
    df.index = pd.to_datetime(df.index)
    # find exact date in df
    try:
        stream = df.loc[pd.to_datetime('today').normalize().date().isoformat()]["Country"]
        return stream
    except KeyError:
        return "NOCOUNTRY"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>F1 Stream Selector</title></head>", "utf-8"))
        if self.path == "/stream_today":
            stream = get_stream_today()
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes(f"<p>{stream}</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == "/country_today":
            country = get_stream_today()
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes(f"<p>{country}</p>", "utf-8"))
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
