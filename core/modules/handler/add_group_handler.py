from config import Config

def init(update, context):
    for member in update.message.new_chat_members:
        if member.username == "@thenebulabot":
            update.message.reply_text('banana')          