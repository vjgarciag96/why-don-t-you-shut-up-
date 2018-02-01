from telegram.ext import CommandHandler
from telegram.ext import Updater
from keys import TOKEN
from commands import shutup

if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    shut_up_command_handler = CommandHandler('shutup', shutup)
    dispatcher.add_handler(shut_up_command_handler)

    updater.start_polling()