#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright hersel91 <hersel1991@gmail.com>
# Copyright SteelManIta


# Python import for error handler and logging
import logging
from datetime import datetime
from core.utility import error_handler

# Import telegram library
from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    CallbackQueryHandler,
    ConversationHandler, 
    Filters)

# Import local files
import plugins
from config import Config
from core.modules import commands,handler

timestamp = datetime.strftime(datetime.today(), '%H:%M at %d/%m/%Y')
print("Start Bot {}".format(timestamp))

# This enables the logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
#########################################################################
#                           USER COMMAND                                #
#       Here I "create" the commands and assign a function              #
#########################################################################

def commandHandler(dispatcher):
    dispatcher.add_handler(CommandHandler("start", commands.user.start.init))
    dispatcher.add_handler(CommandHandler(commands.user.rules.activationWords, commands.user.rules.action))
    dispatcher.add_handler(CommandHandler("aiuto", commands.user.help.init))
    dispatcher.add_handler(CommandHandler("source", commands.user.source.init))
    dispatcher.add_handler(CommandHandler("io", commands.user.io.init))
    dispatcher.add_handler(CommandHandler("distro", commands.user.distro.init))
    dispatcher.add_handler(CommandHandler("richiedi", commands.user.request_function.init))
    dispatcher.add_handler(CommandHandler("feedback", commands.user.feedback.init))
    dispatcher.add_handler(CommandHandler("traduci", commands.user.translate.init))
    dispatcher.add_handler(CommandHandler("google", commands.user.search_google.init))
    dispatcher.add_handler(CommandHandler("cerca", commands.user.search_qwant.init))
    dispatcher.add_handler(CommandHandler("meteo", commands.user.weather.init))
    dispatcher.add_handler(CommandHandler("wikipedia", commands.user.define.init))
    
#########################################################################
#                           ADMIN COMMAND                               #
#                   Decorator: @decorator.admin.init                    #
#                   Source: /core/decorators/admin.py                   #
#                                                                       #
#########################################################################
    dispatcher.add_handler(CommandHandler("ban", commands.admin.ban.init))
    dispatcher.add_handler(CommandHandler("superban", commands.admin.superban.init))
    dispatcher.add_handler(CommandHandler("silenzia", commands.admin.silence.init))
    dispatcher.add_handler(CommandHandler("desilenzia", commands.admin.unsilence.init))
    dispatcher.add_handler(CommandHandler("badword", commands.admin.insert_bad_words.init))
    dispatcher.add_handler(CommandHandler("kick", commands.admin.kick.init))
    dispatcher.add_handler(CommandHandler("info", commands.admin.get.init))
    dispatcher.add_handler(CommandHandler("setbattuta", commands.admin.insert_joke.init))
    dispatcher.add_handler(CommandHandler("setrisposta", commands.admin.insert_custom_handler.init))
    dispatcher.add_handler(CommandHandler("muta", commands.admin.mute.init))
    dispatcher.add_handler(CommandHandler("smuta", commands.admin.unmute.init))
    dispatcher.add_handler(CommandHandler("fissa", commands.admin.pin.init))
    dispatcher.add_handler(CommandHandler("say", commands.admin.say.init))
    dispatcher.add_handler(CommandHandler("a", commands.admin.announcement.init))
    dispatcher.add_handler(CommandHandler("setwelcome", commands.admin.insert_welcome.init))
    dispatcher.add_handler(CommandHandler("updatewelcome", commands.admin.update_welcome.init))
    dispatcher.add_handler(CommandHandler("listwelcome", commands.admin.list_welcome.init))
    dispatcher.add_handler(CommandHandler("setfissa", commands.admin.set_pin.init))
    dispatcher.add_handler(CommandHandler("add", commands.admin.add_buttons.init))
    dispatcher.add_handler(CommandHandler("delete", commands.admin.delete_command.init))
    dispatcher.add_handler(CommandHandler("setrules", commands.admin.set_rules.init))
    dispatcher.add_handler(CommandHandler("badlist", commands.admin.list_badwords.init))

#########################################################################
#                           OWNER COMMAND                               #
#                   Decorator: @decorator.owner.init                    #
#                   Source: /core/decorators/owner.py                   #
#                                                                       #
#########################################################################
    dispatcher.add_handler(CommandHandler("exit", commands.owner.leave.init))
    dispatcher.add_handler(CommandHandler("server", commands.owner.server.init))
    dispatcher.add_handler(CommandHandler("test", commands.owner.test.init))

#########################################################################
#                           PLUGINS MODULES                             #
#                                                                       #
#                           Source: /plugins                            #
#                                                                       #
#########################################################################
    dispatcher.add_handler(CommandHandler("example", plugins.example.init))
    






#########################################################################
#                CALLBACKQUERY HANDLER(Buttons Update)                  #
#########################################################################
def callbackQueryHandler(dispatcher):
    dispatcher.add_handler(CallbackQueryHandler(handler.admin_command.resolved, pattern='resolved'))

#########################################################################
#                              MAIN_HANDLER                             #
#               Source: /core/modules/handler/main_handler.py           #
#        Here we call the functions without a command, => handler       #
#########################################################################
def messageHandler(dispatcher):
    dispatcher.add_handler(MessageHandler(None, handler.main_handler.init))
    
# This is the function that initializes the bot
def main():
    updater = Updater(Config.BOT_API, use_context=True)
    dp = updater.dispatcher
    #########################################################################
    #                          FILTERS HANDLER                              #
    ######################################################################### 
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, handler.welcome.init))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("list", handler.delete_buttons.init)],
        states={
            handler.delete_buttons.RECEIVE_ID: [MessageHandler(Filters.text & (~ Filters.command), handler.delete_buttons.receive_id)]
        },
        fallbacks=[CommandHandler("cancel", handler.delete_buttons.cancel)]
    )
    dp.add_handler(conv_handler)
    commandHandler(dp) 
    callbackQueryHandler(dp)
    messageHandler(dp)


#########################################################################
#                          ERROR HANDLER                                #
#########################################################################
    dp.add_error_handler(error_handler.error)
    
#########################################################################
#                  START POLLING TELEGRAM API                           #
#########################################################################   
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()