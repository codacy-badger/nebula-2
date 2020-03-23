import core.decorators
from config import Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@core.decorators.public_command.init
def init(update, context):
    bot = context.bot
    
    keyboard = [[InlineKeyboardButton("Approva la richiesta✅", callback_data='update_yes'),
                 InlineKeyboardButton("Non approvare la richiesta❌", callback_data='update_no')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    chatid = str(update.message.chat.id)[3:]
    update.message.reply_text("<b>Hai inviato correttamente la richiesta!\nAttendi che un admin ti risponda</b>",parse_mode='HTML')
    bot.send_message(Config.STAFF_GROUP,
    text="<b>RICHIESTA DI PUBBLICITÀ!</b>\nAutore: {username}\nChat: {chat_title}\nLink: {linkurl}{chatid}/{msgid}"
    .format(
    username="@"+update.message.from_user.username,
    msgid=update.message.message_id,
    chat_title=update.message.chat.title,
    chatid=chatid,
    linkurl="https://t.me/c/"),
    parse_mode='HTML', 
    reply_markup=reply_markup)
    
    bot.send_message(Config.LOG_CHANNEL,
    text="<b>RICHIESTA DI PUBBLICITÀ!</b>\nAutore: {username}\nChat: {chat_title}\nLink: {linkurl}{chatid}/{msgid}"
    .format(
    username="@"+update.message.from_user.username,
    msgid=update.message.message_id,
    chat_title=update.message.chat.title,
    chatid=chatid,
    linkurl="https://t.me/c/"),
    parse_mode='HTML')

@core.decorators.admin.init
def update_yes(update, context):
    query = update.callback_query
    query.edit_message_text(text="<b>Approvato dall'admin: @{username}</b>"
    .format(username=str(update.effective_user.username)),parse_mode='HTML')

@core.decorators.admin.init
def update_no(update, context):
    query = update.callback_query
    query.edit_message_text(text="<b>Non Approvato dall'admin: @{username}</b>"
    .format(username=str(update.effective_user.username)),parse_mode='HTML')