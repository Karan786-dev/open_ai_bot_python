import requests
from config import *


class Bot:
    def __init__(self, bot_token, webhook_url):
        if not bot_token:
            raise Exception("Please provide Bot Token")
        if not webhook_url:
            raise Exception("Please provide webhook url")
        self.bot_token = bot_token
        self.webhook_url = webhook_url
        self.telegram_bot_api = telegram_bot_api + bot_token
        return

    def start(self):
        self.deleteWebhook()
        self.setWebhook()
        pass

    def setWebhook(self):
        r = requests.post(
            url=f"{self.telegram_bot_api}/setWebhook", params={"url": webhook_url}
        ).json()
        if not r["ok"]:
            raise Exception(r)
        else:
            return r

    def deleteWebhook(self):
        r = requests.post(url=f"{self.telegram_bot_api}/deleteWebhook").json()
        if not r["ok"]:
            raise Exception(r)
        else:
            return r

    def getMe(self):
        r = requests.post(url=f"{self.telegram_bot_api}/getMe").json()
        if not r["ok"]:
            raise Exception(r)
        else:
            return r["result"]

    def sendMessage(self, data):
        r = requests.post(url=f"{self.telegram_bot_api}/sendMessage",params=data).json()
        if not r["ok"]:
            raise Exception(r)
        else:
            return r["result"]
    def sendPhoto(self,data):
        r = requests.post(url=f"{self.telegram_bot_api}/sendPhoto",params=data).json()
        if not r["ok"]:
            raise Exception(r)
        else:
            return r["result"]
