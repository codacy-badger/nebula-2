#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright hersel91 <hersel1991@gmail.com>
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utility import utils
from telegram import ChatPermissions
from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Welcome
from core.sql.commands_sql import Sql_Buttons
from core.utility.strings import str_service

@run_async
def init(update, context):
    bot = context.bot
    for member in update.message.new_chat_members:
        if member.username is not None:
            connector = Connection()
            chatid = str(update.message.chat_id)
            query = Sql_Welcome.SQL
            connector.cur.execute(query,[chatid])
            row = connector.cur.fetchone()
            if row is not None:
                parsed_message = row[0].replace('{first_name}',
		        update.message.from_user.first_name).replace('{chat_name}',
		        update.message.chat.title).replace('{username}',
		        "@"+member.username)
                connector = Connection()
                db_query = Sql_Buttons.SQL_1
                connector.cur.execute(db_query,[chatid])
                rows = connector.cur.fetchall()
                buttons = []
                for link in rows:
                    buttons.append(InlineKeyboardButton(text=link[1], url=link[2]))
                menu = utils.build_menu(buttons, 2)
                welcome_message = "{}".format(parsed_message)
                update.message.reply_text(welcome_message, reply_markup=InlineKeyboardMarkup(menu), parse_mode='HTML')
            else:
                bot.send_message(update.message.chat_id, str_service.DEFAULT_WELCOME.format(username="@"+member.username,chat=update.message.chat.title))

        else:
            bot.send_message(update.message.chat_id,"{} imposta un username!\nSei stato kickato per sicurezza!"
                             .format(update.message.from_user.id))
            bot.kick_chat_member(update.message.chat_id,update.message.from_user.id)