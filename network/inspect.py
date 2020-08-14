#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
network = mydata.getvalue("net_name")

output = subprocess.getoutput("sudo docker network inspect " + network )
print(output)
