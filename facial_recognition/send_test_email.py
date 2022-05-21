#! /usr/bin/python

# Imports
import requests

def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd0830df8d79b47e4bfe3f26f76dcb117.mailgun.org",
        auth=("api", "a460a2a691016765ff32968c7d464e4d-62916a6c-bdd99cd0"),
        data={"from": 'r0882112@student.thomasmore.be',
            "subject": "Visitor Alert",
            "html": "<html> Your Raspberry Pi recognizes someone. </html>"})
                      
request = send_simple_message()
print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))
