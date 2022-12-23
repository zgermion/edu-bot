import message
import database

def lesson_list(words, chat_id):
    print(len(words))
    if(len(words)>2):
        message.send_message(chat_id, "Слишком много параметров!")
    elif(len(words)==2):
        try:
            database.get_lesson(int(words[1]), chat_id, False)
        except:
            message.send_message(chat_id, "😡 Номер урока может быть только целым положительным числом или такого урока еще нет :)")
    elif(len(words)==1):
        database.get_lesson(0, chat_id, True)

def addlesson(text_message, user_id, chat_id):
    document_admin = database.collection_user.find({"nickname": user_id})

    words = text_message.split()

    if(document_admin[0]["status"] == "admin"):
        if(len(words)<2):
            message.send_message(chat_id, "🛑 Укажите тему и текст урока!")
        elif(len(words)<3):
            message.send_message(chat_id, "🛑 Укажите текст урока!")
        else:
            theme_lesson = words[1]
            text_lesson = text_message[12+len(theme_lesson):]
            author_lesson = user_id

            document_lesson = database.collection_lesson.find({})
            document_lesson = list(document_lesson)

            number_lesson = document_lesson[len(document_lesson)-1]["number"]+1

            database.collection_lesson.insert_one( {"number" : number_lesson, "author" : author_lesson, "name" : theme_lesson, "text" : text_lesson})

            message.send_message(chat_id, "✅ Статья добавлена")
    else:
        message.send_message(chat_id, "🛑 Вы не администратор и не можете внести изменение!")