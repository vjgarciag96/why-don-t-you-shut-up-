from telegram.ext import BaseFilter

class UserFilter(BaseFilter):
    def filter(self, message):
        print(message)
        if message.from_user.username != None:
            return message.from_user.username == 'username'
        else:
            return False