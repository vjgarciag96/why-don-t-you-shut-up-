from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from keys import TOKEN
from commands import shutup
from messages import drop_message

if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    shut_up_command_handler = CommandHandler('shutup', shutup)
    dispatcher.add_handler(shut_up_command_handler)

    delete_messages_handler = MessageHandler(Filters.text, drop_message)
    dispatcher.add_handler(delete_messages_handler)

    updater.start_polling()