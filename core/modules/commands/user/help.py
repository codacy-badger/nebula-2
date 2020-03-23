from config import Config
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Help

def init(update, context):
    bot = context.bot
    connector = Connection()
    query = Sql_Help.SQL
    connector.cur.execute(query)
    row = connector.cur.fetchone()
    help_message = "{}\n\nRelease info: {source}".format(row[0],source=Config.SOURCE)
    bot.send_message(update.message.chat_id,help_message, parse_mode='HTML')