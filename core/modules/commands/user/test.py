import core.decorators

@core.decorators.admin.user_admin
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id, text="ciao")