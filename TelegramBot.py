# Telgeram bot needs "python-telegram-bot" library, which you will need to install using pip command.
# pip install python-telegram-bot

import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Your Token from bot fahter
TOKEN = "Your_Token"

#List of Sharable PDFs
pdf_files = ['Names_of_Sharable_PDF']

def start(update, context):
    update.message.reply_text("Your_Message")
    
def pdf(update, context):
    global is_found
    is_found = True                #defining Flag
    file_name = " ".join(context.args)
    for file in pdf_files:
       if file == file_name:
        update.message.reply_text("Getting your file...")
        context.bot.sendDocument(update.effective_chat.id,document=open(file_name+'.pdf','rb'))
        is_found = False
        break                           #If File found Break the Loop
    
    if is_found:
        update.message.reply_text("Sorry, I don't have that PDF file. Please make sure you spelled the name correctly.") 


updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add the command handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("pdf", pdf))

# Start the bot
updater.start_polling()
updater.idle()
