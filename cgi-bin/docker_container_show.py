#!/usr/bin/python3
print("content-type: text/html")
print()
import cgi
import subprocess

output = subprocess.getoutput('sudo podman ps')
print("<pre>")
print(output)
print("</pre>")
