import core.decorators

@core.decorators.owner.init
def init(update, context):
  bot = context.bot
  bot.send_message(update.message.chat_it, text="OWNER COMMAND TEST")