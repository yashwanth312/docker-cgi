#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
volume = mydata.getvalue("new_vol")

output = subprocess.getoutput("sudo docker volume create " + volume)
print(output)
