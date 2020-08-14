#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
contname = mydata.getvalue("cont_name")
imgname = mydata.getvalue("img_name")

output = subprocess.getoutput("sudo docker commit " + contname + " " + imgname)
print(output)

