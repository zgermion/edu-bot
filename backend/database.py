import pymongo
import config
import message

client = pymongo.MongoClient(config.TOKEN_DB)

database_logs = client[config.DB_logs]
coll_logs = database_logs[config.DB_logs_umessage]

database_lesson = client[config.DB_lesson]
collection_lesson = database_lesson[config.COLL_lesson]

database_user = client[config.DB_user]
collection_user = database_user[config.COLL_user]



def create_logs(user_id, message, time):
    coll_logs.insert_one( {"user_id" : user_id, "message" : message, "time" : time})
    print("[", time, "][", user_id, "]: ", message)

def get_lesson(num_lesson, chat_id, is_main):
    if(is_main==True):
        text = "🎓Список уроков:\n"
        cursor = collection_lesson.find({})
        for document in cursor:
            text = text+"\n"+f"{document['number']}. Тема: {document['name']}"
        message.send_message(chat_id, text)
    else:
        document = collection_lesson.find({"number": num_lesson})
        message.send_message(chat_id, f"📕 Урок {document[0]['number']}. Тема: {document[0]['name']} \n \n{document[0]['text']}\n\n🧑‍🏫Автор:  {document[0]['author']}")