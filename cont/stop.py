#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
contstp = mydata.getvalue("stp_cont")

output = subprocess.getoutput("sudo docker stop " + contstp)
print(output)

