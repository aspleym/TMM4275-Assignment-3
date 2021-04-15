from Python.Maze import Maze
from Python.generateDFA import generateDFA
import http.server
import json
import socketserver
import os
import re
import time
import math
from Python.fusekiposter import *

IP_NUMBER = '127.0.0.1'
PORT_NUMBER = 8080


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # Redirects to main page
        if self.path == '/':
            self.path = '/Wall-E/index.html'
            
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_type = self.headers['content-type']
        if not content_type:
            return (False, "Content-Type header doesn't contain boundary")
        boundary = content_type.split("=")[1].encode()
        if boundary.decode('utf-8').lower() == 'utf-8':
            # We got one of the predefined mazes
            # Gets the file name:
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len)
            post_string = post_body.decode('utf-8')
            parameters = post_string.split("&")
            mazeUrl = parameters[0]
            name = mazeUrl
        else:
            # We got a custom csv
            # Stores the file on the server and returs the file name
            r, info, path = self.deal_post_data(boundary)
            name = path.split('/')[-1]
        # Creating a maze from csv file
        m = Maze(name)
        # Generating trajectory
        m.getTrajectory()
        # Posting trajectory to fuseki
        postTrajectory(name.removesuffix(".csv"), m.trajectory)
        # Generating a dfa containing the maze and the trajectory from fuseki
        generateDFA(name)
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    # Helper function to store the custom csv on the server
    def deal_post_data(self, boundary):
        
        remainbytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remainbytes -= len(line)
        if not boundary in line:
            return (False, "Content NOT begin with boundary")
        line = self.rfile.readline()
        remainbytes -= len(line)
        fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line.decode())
        if not fn:
            return (False, "Can't find out file name...")
        name = fn
        path = self.translate_path(self.path)
        rel_path = "Maze/Uploaded/" + fn[0]
        fn = os.path.join(path, rel_path)
        line = self.rfile.readline()
        remainbytes -= len(line)
        line = self.rfile.readline()
        remainbytes -= len(line)
        try:
            out = open(fn, 'wb')
        except IOError:
            return (False, "Can't create file to write, do you have permission to write?")
                
        preline = self.rfile.readline()
        remainbytes -= len(preline)
        while remainbytes > 0:
            line = self.rfile.readline()
            remainbytes -= len(line)
            if boundary in line:
                preline = preline[0:-1]
                if preline.endswith(b'\r'):
                    preline = preline[0:-1]
                out.write(preline)
                out.close()
                return (True, "Upload success!", "%s" % fn)
            else:
                out.write(preline)
                preline = line
        return (False, "Unexpect Ends of data.")

        


Handler = MyRequestHandler
# Set server to localhost and port 8080
server = socketserver.TCPServer((IP_NUMBER, PORT_NUMBER), Handler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
