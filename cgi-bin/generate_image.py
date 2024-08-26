#!/usr/bin/env python3

import cgi
import cgitb
import requests
import base64

cgitb.enable()


print("Content-Type: text/html\n")

form = cgi.FieldStorage()
prompt = form.getvalue('prompt')

if prompt:
    api_key = ""
    api_url = ""

    headers = {
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    }

    data = {
        "prompt": prompt,
        "output_format": "jpeg"
    }

    response = requests.post(api_url, headers=headers, files={"none": ''}, data=data)

    if response.status_code == 200:
        img_data = base64.b64encode(response.content).decode('utf-8')
        print(f'<img src="data:image/jpeg;base64,{img_data}" alt="Generated Image">')
    else:
        print("<p>Error generating image: {}</p>".format(response.json()))
else:
    print("<p>Error: No prompt provided.</p>")