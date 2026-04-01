import requests

class IPFSClient:

    def __init__(self, url="http://127.0.0.1:5001/api/v0/add"):
        self.url = url

    def subir(self, contenido):
        files = {
            'file': ('idea.txt', contenido)
        }

        res = requests.post(self.url, files=files)
        return res.json()["Hash"]
