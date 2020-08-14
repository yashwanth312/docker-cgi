#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
contstr = mydata.getvalue("str_cont")

output = subprocess.getoutput("sudo docker start " + contstr)
print(output)
