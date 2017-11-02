from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import sys

path = sys.stdin.readline()
authorizer = DummyAuthorizer()
authorizer.add_anonymous(path[:-1], perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

servip = sys.stdin.readline()
port = sys.stdin.readline()
server = FTPServer((servip[:-1], int(port[:-1])), handler)
server.serve_forever()
