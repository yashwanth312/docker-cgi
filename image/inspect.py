#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
img = mydata.getvalue("img_name")

output = subprocess.getoutput("sudo docker image inspect " + img)
print(output)

