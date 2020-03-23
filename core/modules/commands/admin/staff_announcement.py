import core.decorators
from config import Config

@core.decorators.admin.init
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    var_messaggio = update.message.text[14:]
    bot.send_message(Config.STAFF_GROUP, text="{}\n@Hersy @TheLonelyAdventurer @jfet97 @thecmo @SteelManITA @iAmGio @Folgore796"
                     .format(var_messaggio))