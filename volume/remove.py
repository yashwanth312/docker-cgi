#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
volume = mydata.getvalue("rm_vol")

output = subprocess.getoutput("sudo docker volume rm " + volume)
print(output)
