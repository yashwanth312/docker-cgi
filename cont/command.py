#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
cont = mydata.getvalue("cmd")
contname = mydata.getvalue("cont_name")

output = subprocess.getoutput("sudo docker exec " + contname + " " + cont)  
print(output)

