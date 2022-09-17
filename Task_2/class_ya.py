import requests


class Yandex:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_directory(self, dir_name):
        headers = self.get_headers()
        params = {'path': dir_name}
        response = requests.put(self.url, headers=headers, params=params)
        return dir_name, response.status_code
