import core.decorators
import wikipedia as wiki
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utility import utils

@core.decorators.public_command.init
def init(update, context):
    bot = context.bot
    # Recupero della definizione
    arg = update.message.text[16:]
    wiki.set_lang('it')
    try:
        pg = wiki.page(wiki.search(arg)[0])
        title = pg.title
        pg_url = pg.url
        definizione = pg.summary
        button_list = [InlineKeyboardButton("Guarda su Wikipedia", url=pg_url)]
        reply_markup = InlineKeyboardMarkup(utils.build_menu(button_list, n_cols=1))
        text = "*{}:*\n\n{}".format(title, definizione)
        update.message.reply_markdown(text, reply_markup=reply_markup)
    except:
        bot.send_message(update.message.chat_id, text="Mi spiace {user} non ho trovato quello che cercavi"
                                 .format(user=update.message.from_user.first_name))