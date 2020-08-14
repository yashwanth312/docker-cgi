#!/usr/bin/python3

import subprocess

print("content-type: text/html")
print()

output = subprocess.getoutput("sudo docker network ls")
print(output)
