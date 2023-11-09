import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def register_account_in_shapes():

    url = "https://kubernetes.pasiphae.eu/shapes/asapa/auth/register"

    payload = json.dumps({
        "email": os.getenv('EMAIL'),
        "password": os.getenv('PASSWORD'),
        "metadata": {
            "smart_caring": "smart caring app"
        }
    })
    headers = {
        'X-Shapes-Key': os.getenv('SHAPES_KEY'),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    return response.text


def login_account_in_shapes():
    url = "https://kubernetes.pasiphae.eu/shapes/asapa/auth/login"

    payload = json.dumps({
        "email": os.getenv('EMAIL'),
        "password": os.getenv('PASSWORD')
    })
    headers = {
        'X-Shapes-Key': os.getenv('SHAPES_KEY'),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.text


def main():
    #  First step is to register the account in shapes
    response = register_account_in_shapes()
    print(response)

    #  Second step is to make login in shapes
    response = login_account_in_shapes()
    print(response)

if __name__ == '__main__':
    main()
