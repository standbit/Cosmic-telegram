import os
from dotenv import load_dotenv
from telegram.ext import Updater
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import telegram


load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

updater = Updater(TG_TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

bot = telegram.Bot(token=TG_TOKEN)
tg_chat_id = '@cosmosfromphoto'
bot.send_message(chat_id=tg_chat_id, text="Hi, everyone!")

updater.start_polling()
updater.idle()