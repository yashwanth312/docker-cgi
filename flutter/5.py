#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
imgname = mydata.getvalue("img_name")
netname = mydata.getvalue("net_name")

output = subprocess.getoutput("sudo " + "docker run -dit --network " + netname + " " + imgname)
print(output)
