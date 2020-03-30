from config import Config
from core.utility import utils
from . import (
    admin_command, 
    joke, 
    custom_handler,
	send_nudes, 
    bad_words, 
    welcome,
	super_ban_handler
    )

msg = ""

def trigger(match):
	return msg.lower().startswith(match.lower())

#FUNCTION DECLARATION
def init(update, context):
	global msg #pylint: disable=global-statement


	bad_words.init(update, context)
	super_ban_handler.init(update, context)
	
	if update.message is None or update.message.text is None:
		return

	msg = update.message.text

	if trigger("{} send nudes".format(Config.BOT_NAME)):
		send_nudes.init(update, context)
	elif trigger("{} fai una battuta".format(Config.BOT_NAME)):
		joke.init(update, context)
	elif trigger("@admin"):
		admin_command.init(update, context)
	elif trigger(Config.BOT_NAME):
		custom_handler.customhandler(update, context)
	elif trigger("/"):
		custom_handler.customhandler(update, context)