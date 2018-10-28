#import requests
#import os

import random
import string
import json

chars = string.ascii_letters + string.digits + "!@#$%^&*"

emails = ("@yahoo.com","@gmail.com","@aol.com","@hotmail.com")

names = json.loads(open('S:\\Users\\Khaswi\\Documents\\python_stuff\\python_re_scam\\names.json').read())

for name in names:
    extra = ''.join(random.choice(string.digits))
    extra2 = ''.join(random.choice(string.digits))
    username = name.lower() + extra + extra2 + random.choice(emails)
    password = "".join(random.choice(chars) for i in range(8))
    print("Username: {:30s}  Password: {}".format(username,password))


#adding test change 1