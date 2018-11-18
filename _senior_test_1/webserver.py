import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler
webdir='.'
port = 80
os.chdir(webdir)
a = os.getcwd()
print(a)
srvraddr = ("", port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()