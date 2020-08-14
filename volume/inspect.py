#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
volume = mydata.getvalue("vol_name")

output = subprocess.getoutput("sudo docker volume inspect " + volume)
print(output)


