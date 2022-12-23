from flask import Flask, request
import requests
import json
import config
import database
import message
import datetime
import lesson
import account

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        if(list(request.json)[1] == "message"):

            text_message = request.json["message"]["text"]
            user_id = request.json["message"]["chat"]["username"]
            time = datetime.datetime.now()
            chat_id = request.json["message"]["chat"]["id"]

            database.create_logs(user_id, text_message, time)

            words = text_message.split()
            if(words[0] == '/start'):
                account.add_user(user_id)
                message.send_message(chat_id, "✨Привет! Рады видеть тебя в нашем образовательном боте! \n \nНа данный момент я поддерживаю следующие команды: \n \n1️⃣ /lesson <номер урока> - введи просто /lesson, если хочешь увидеть список всех уроков.\n\n2️⃣ /account - информация о твоем аккаунте")
            elif(words[0] == "/lesson"):
                lesson.lesson_list(words, chat_id)
            elif(words[0] == "/account"):
                account.send_account_info(user_id, chat_id)
            elif(words[0] == "/addperms"):
                account.addperms(words, user_id, chat_id)
            elif(words[0] == "/addlesson"):
                lesson.addlesson(text_message, user_id, chat_id)
            else:
                message.send_message(chat_id, "🙈 К сожалению такой команды пока что нет :(")
    return {"ok": True}