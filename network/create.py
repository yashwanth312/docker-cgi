#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
network = mydata.getvalue("new_net")


output = subprocess.getoutput("sudo docker network create " + network) 
print(output)
