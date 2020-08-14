#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
imgname = mydata.getvalue("img_name")
netname = mydata.getvalue("net_name")
port = mydata.getvalue("ports")
svpath = mydata.getvalue("sv_path")
dvpath = mydata.getvalue("dv_path")

output = subprocess.getoutput("sudo docker run -dit -p " + port + " --network " + netname + " -v " + svpath + ":" + dvpath + " " + imgname)
print(output)
