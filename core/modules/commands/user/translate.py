from config import Config
from flaky import flaky
from yandex.Translater import Translater

@flaky(3, 1)
def init(update, context):
    bot = context.bot
    message_var = update.message.text[8:]
    try:
        tr = Translater()
        tr.set_key(Config.YANDEX_API) # Api key found on https://translate.yandex.com/developers/keys
        tr.set_text(message_var)
        tr.set_from_lang('it')
        tr.set_to_lang('en')
        bot.send_message(update.message.chat_id, tr.translate())
    except:
        bot.send_message(update.message.chat_id,text="Perfavore inserisci una frase.")        