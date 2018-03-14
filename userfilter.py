from telegram.ext import BaseFilter

BANNED_USERS = ["PerillaRela"]
BANNED_WORDS = ["Twitch"]


class UserFilter(BaseFilter):
    def filter(self, message):
        return message.from_user.username in BANNED_USERS and any(word in message.text for word in BANNED_WORDS)
