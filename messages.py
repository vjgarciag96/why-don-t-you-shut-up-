from keys import TOKEN

BASE_URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def drop_message(bot, update):
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    bot.delete_message(chat_id, message_id)
