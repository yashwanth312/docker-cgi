#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
doimg = mydata.getvalue("down_img")

output = subprocess.getoutput("sudo docker pull " + doimg)
print(output)


