#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
network = mydata.getvalue("rm_net")

output = subprocess.getoutput("sudo docker network rm " + network)
print(output)

