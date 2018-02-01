import urllib.request
from keys import TOKEN

BASE_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def drop_message(bot, update):
    print('executing drop message')
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    url = BASE_URL + "deleteMessage?chat_id={}&message_id={}".format(chat_id, message_id)
    response = urllib.request.urlopen(url).read()
    print(response)
