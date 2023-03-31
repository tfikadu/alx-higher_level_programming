#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""

import requests

if __name__ == "__main__":
    content = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
