# Telgeram bot needs "python-telegram-bot" library, which you will need to install using pip command.
# pip install python-telegram-bot

import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "Your_Token"

def start(update, context):
    update.message.reply_text("Your_Message")
    
def pdf(update, context):
    


updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add the command handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("pdf", pdf))

# Start the bot
updater.start_polling()
updater.idle()
