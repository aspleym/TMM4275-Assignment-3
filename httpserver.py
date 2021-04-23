from Python.generateNXFile import createNXFile
from Python.mail import *
import http.server
import socketserver
import os
import re

IP_NUMBER = '127.0.0.1'
PORT_NUMBER = 8080


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # Redirects to main page
        if self.path == '/':
            self.path = '/WC/index.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_type = self.headers['content-type']
        if not content_type:
            return (False, "Content-Type header doesn't contain boundary")
        boundary = content_type.split("=")[1].encode()
        if boundary.decode('utf-8').lower() == 'utf-8': # We got the info as text, and will store it as a .ini file
            
            # Gets the file name:
            content_len = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_len)
            post_string = post_body.decode('utf-8')
            parameters = post_string.split("&")
            info = parameters[0]
            print("Info!")
            temp = info
            name = temp.removeprefix("NAME: ").split("\n")[0].split(".")[0]
            path = os.path.join(self.translate_path(self.path), f'Products/{name}/')
            configName = name + ".ini"
            fn = os.path.join(path, configName)
            print(info) # "filename \n email \n L \n W \n H"
            iniFile = open(fn, "w")
            iniFile.write(info)
            iniFile.close()  
            
            createNXFile(name, PASSWORD)
  
            temp = info
            adress = temp.split("\n")[1].removeprefix("EMAIL: ")
            subject = 'Your WC Design has been submitted'
            body = f"<p>Your design {name} is now submitted and is waiting for a designer to process it</p>"
            sendMailToClient(adress, PASSWORD, subject, body)
            # The designer notification is disabled as we don't have an adress to sent it to
            # sendMailToDesigner(adress, PASSWORD, subject, body)


            
        else:
            # We got the .prt file
            # Stores the file on the server and returs the file name
            r, info, path = self.deal_post_data(boundary)
            print(info)
            print("fn was: ", path)
            #name = path.split('/')[-1]

        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    # Helper function to store the .prt file on the server

    def deal_post_data(self, boundary):

        remainbytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remainbytes -= len(line)
        if not boundary in line:
            return (False, "Content NOT begin with boundary", "%s" % fn)
        line = self.rfile.readline()
        remainbytes -= len(line)
        fn = re.findall(
            r'Content-Disposition.*name="file"; filename="(.*)"', line.decode())
        if not fn:
            return (False, "Can't find out file name...", "%s" % fn)

        path = self.translate_path(self.path)
        folderPath = os.path.join(path, f'Products/{fn[0].split(".")[0]}/')
        print(folderPath)
        print(fn[0])
        try:
            os.mkdir(folderPath)
        except:
            print("Folder already exists.")
        fn = os.path.join(folderPath, fn[0])
        line = self.rfile.readline()
        remainbytes -= len(line)
        line = self.rfile.readline()
        remainbytes -= len(line)
        print(fn)
        try:
            out = open(fn, 'wb')
        except IOError:
            return (False, "Can't create file to write, do you have permission to write?", "%s" % fn)

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

                # TODO: Python template changed
                return (True, "Upload success!", "%s" % fn)
            else:
                out.write(preline)
                preline = line
        return (False, "Unexpect Ends of data.", "%s" % fn)

print("Please enter the password for the designer mail account.\
    \nYou can find this in the submission on Blackboard.\
    \nPress *ENTER* if you don't want to use the mail functionality (not recommended):")

PASSWORD = str(input())



Handler = MyRequestHandler
# Set server to localhost and port 8080
server = socketserver.TCPServer((IP_NUMBER, PORT_NUMBER), Handler)
print("Server started successfully")

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
