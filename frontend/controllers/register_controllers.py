import requests

from frontend.config import URL_FOR_LOGIN


def mylogin(username, password):
    response = requests.post(URL_FOR_LOGIN, json={'username': username, 'password': password})
    if response.status_code == 200:
        return True, response.json()
    else:
        return False, response.json()