def shutup(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Ha sido usted spameado")
