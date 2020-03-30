import core.decorators
from core.sql.db_connect import Connection

@core.decorators.owner.init
def init(update, context):
  bot = context.bot
  chatid = str(update.message.chat_id)
  connector = Connection()
  query = "SELECT language_set FROM language WHERE id_group = %s"
  connector.cur.execute(query,[chatid])
  row = connector.cur.fetchone()
  print(row[0])
  if row[0] == "IT":
    bot.send_message(update.message.chat_id, text= "ITALIANO")
  if row[0] == "EN":
    bot.send_message(update.message.chat_id, text="ENGLISH")