import core.decorators
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utility import utils
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Buttons

@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    connector = Connection()
    query = Sql_Buttons.SQL_1
    connector.cur.execute(query)
    rows = connector.cur.fetchall()
    buttons = []
    for link in rows:
        buttons.append(InlineKeyboardButton(text=link[1], url=link[2]))
    menu = utils.build_menu(buttons, 2)
    bot.send_message(update.message.chat_id,"Le Nostre Community su Telegram:",
                     reply_markup=InlineKeyboardMarkup(menu))