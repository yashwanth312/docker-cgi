#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()


mydata = cgi.FieldStorage()
imgname = mydata.getvalue("img_name")
contname = mydata.getvalue("cont_name")

output = subprocess.getoutput("sudo " + "docker run -dit --name " + contname + " " + imgname)

print(output)
