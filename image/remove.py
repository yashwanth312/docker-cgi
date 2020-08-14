#!/usr/bin/python3

import subprocess 
import cgi

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
doimg = mydata.getvalue("rm_name")

output = subprocess.getoutput("sudo docker image rm  " + doimg)
print(output)

