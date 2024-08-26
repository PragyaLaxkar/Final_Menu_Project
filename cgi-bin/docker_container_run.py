#!/usr/bin/python3
print("content-type: text/html")
print()
import cgi
import subprocess

form = cgi.FieldStorage()
image = form.getvalue("image")
output = subprocess.getoutput('sudo podman run -itd '+ image)
print("<pre>")
print(output)
print("</pre>")
