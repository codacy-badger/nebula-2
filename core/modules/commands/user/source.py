import core.decorators
from config import Config

@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id, text="<b>     NebulaBot</b>\n"
                                          "====================\n\n"
                                          "<b>Linguaggio:</b> <em>Python</em>\n\n"
                                          "<b>Versione</b>:<em>{source}</em>\n\n"
                                          "<b>Developer</b>:<em>{author}</em>\n\n"
                                            "<b>Sorgente</b>:<a href=\"{repo}\"> GitHub</a>\n\n"
                                          "<b>Sito Web</b>:  <a href=\"https://hersel.it\">hersel.it</a> "
                                          .format(source=Config.VERSION,
                                                  repo=Config.SOURCE,
                                                  author=Config.AUTHOR),
                                          parse_mode = 'HTML')