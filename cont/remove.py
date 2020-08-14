#!/usr/bin/python3

import subprocess
import cgi 

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
contrm = mydata.getvalue("rm_cont")

output = subprocess.getoutput("sudo docker rm -f " + contrm)
print(output)
