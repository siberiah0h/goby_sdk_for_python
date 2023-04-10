import requests
import base64
import json

class BasePage:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.session = requests.Session()

    def _send_request(self, path, data):
        authorization = base64.b64encode(f"{self.username}:{self.password}".encode()).decode()
        headers = {
            "Authorization": f"Basic {authorization}",
            "Content-Type": "application/json;charset=UTF-8",
        }
        response = self.session.post(f"{self.url}/{path}", headers=headers, data=json.dumps(data))
        return response.json()

    def _send_get_request(self, path, params=None):
        authorization = base64.b64encode(f"{self.username}:{self.password}".encode()).decode()
        headers = {
            "Authorization": f"Basic {authorization}",
            "Content-Type": "application/json;charset=UTF-8",
        }
        response = self.session.get(f"{self.url}/{path}", headers=headers, params=params)
        return response.json()