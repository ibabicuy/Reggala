#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

from pymongo import MongoClient

import time
import json
##client = MongoClient()
client = MongoClient("mongodb://localhost:27017")


db = client['plants']
plants= db.plants


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def do_GET(self):
        self._set_headers()
        if self.path == "/humidityData":
            plant=plants.find({"plant_id":1})[0]
            print plant
            self.wfile.write(plants.find({"plant_id":1})[0]["humidity_data"])

        elif self.path == "/getCurrentHumidityValue":


            pipeline = [{"$match":
                             {"plant_id": 1}
                         },
                        {"$unwind": "$humidity_threshold"},
                        {"$sort":
                             {"humidity_threshold.date": -1}
                         },
                        {"$limit": 1},
                        {"$project":
                             {"_id": 0, "humidity_threshold.threshold": 1}
                         }
                        ]

            last_threshold=list(plants.aggregate(pipeline))
            if not last_threshold is None:
                last_threshold = last_threshold[0]['humidity_threshold']['threshold']


            self.wfile.write(last_threshold)

        else:
            self.wfile.write("<html><body><h1>Error 404</h1></body></html>")


    def do_POST(self):
        # Doesn't do anything with posted data

        if self.path == "/changeHumidity":
            content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
            post_data = self.rfile.read(content_length)  # <--- Gets the data itself
            self._set_headers()
            timestamp = int(time.time())

            post_data =  json.loads(post_data)
            if "value" in post_data:
                plants.update({"plant_id":1},{"$push":{"humidity_threshold":{"date":timestamp,"threshold":post_data['value']}}})
                self.wfile.write("true")
            else:
                self.wfile.write("false")
        else:
            content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
            self._set_headers()
            self.wfile.write("<html><body><h1>Error 404</h1></body></html>")




def run(server_class=HTTPServer, handler_class=S, port=3080):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()





