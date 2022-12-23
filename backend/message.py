import config
import requests

def send_message(chat_id, text):
    method = "sendMessage"
    url = f"https://api.telegram.org/bot{config.TOKEN}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)