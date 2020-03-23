import core.decorators
from datetime import datetime
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Superban
from core.utility.strings import str_service
from telegram.ext.dispatcher import run_async


@core.decorators.admin.init
@core.decorators.bot_admin.bot_admin
@run_async
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message = str(update.message.text[9:])
    if message != "":
        save_user_id=update.message.reply_to_message.from_user.id
        save_date = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
        connector = Connection()
        query= Sql_Superban.SQL
        connector.cur.execute(query, [save_user_id,message,save_date])
        connector.db.commit()
        bot.send_message(update.message.chat_id,
                         text="Hai SUPERBANNATO {id}"
                         .format(id=update.message.reply_to_message.from_user.id),
                         parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id,str_service.MESSAGE_SB,
                         parse_mode='HTML')