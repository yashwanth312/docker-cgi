#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print() 

mydata = cgi.FieldStorage()
imgname = mydata.getvalue("img_name")

output = subprocess.getoutput("sudo " + "docker run -dit " + imgname)
print(output)
