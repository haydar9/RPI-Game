'''
Created on Sep 17, 2013

@author: haydar
'''
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

#predefined values#
host = socket.gethostname() # Get local machine name
port = 60                # Reserve a port for your service.

s = socket.socket()         # Create a socket object

s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done