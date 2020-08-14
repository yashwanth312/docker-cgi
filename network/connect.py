#!/usr/bin/python3

import cgi 
import subprocess 

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
network = mydata.getvalue("new_net")
cont = mydata.getvalue("cont_name")

output = subprocess.getoutput("sudo docker network connect " + network + " " + cont)
print(output)
