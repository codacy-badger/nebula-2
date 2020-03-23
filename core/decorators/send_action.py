import telegram
from functools import wraps
from time import sleep
from random import random

def init(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_message.chat_id, 
            action=telegram.ChatAction.TYPING)
        sleep(random() * 1 + 1.)
        return func(update, context,  *args, **kwargs)

    return command_func