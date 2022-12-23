import database
import message

def add_user(user_id):
    document = database.collection_user.find({"nickname": user_id})
    if(len(list(document))!=1):
        print(f"Новый пользователь в боте: {user_id}")
        database.collection_user.insert_one( {"nickname" : user_id, "status" : "user"})
    else:
        print(f"{user_id} ранее уже был в боте!")

def send_account_info(user_id, chat_id):
    document = database.collection_user.find({"nickname": user_id})
    if(document[0]['status'] == "user"):
        message.send_message(chat_id, f"🤖 Информация о твоем аккаунте: \n\n👥 Тип доступа: {document[0]['status']}")
    elif(document[0]['status'] == "admin"):
        message.send_message(chat_id, f"🤖 Информация о твоем аккаунте: \n\n👥 Тип доступа: {document[0]['status']}\n\n💥 Твои уникальные команды:\n\n1️⃣/addperms <никнейм> - выдать админку\n2️⃣/addlesson <название темы> <текст темы>")

def addperms(words, user_id, chat_id):
    document_admin = database.collection_user.find({"nickname": user_id})

    if(document_admin[0]["status"] == "admin"):
        if(len(words)<2):
            message.send_message(chat_id, "🛑 Укажите ник человеку, которому необходимо выдать админку")
        else:
            nickname = words[1]
            document_nickname = database.collection_user.find({"nickname": nickname})
            if(len(list(document_nickname.clone()))==0):
                database.collection_user.insert_one({"nickname" : nickname, "status" : "admin"})
                message.send_message(chat_id, "✅ Админка выдана несуществующему акканту :)")
            else:
                if((document_nickname.clone())[0]["status"] == "admin"):
                    message.send_message(chat_id, "🛑 Этот аккаунт уже имеет админку")
                else:
                    database.collection_user.update_one({'_id': document_nickname[0]['_id']},{'$set': {'status': 'admin'}}, upsert=False)
                    message.send_message(chat_id, "✅ Админка выдана акканту :)")
    else:
        message.send_message(chat_id, "🛑 Вы не имеете таких прав!")
