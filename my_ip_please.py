import logging
import socket
import telegram
import config
from telegram.ext import CommandHandler, Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=config.TOKEN)
dispatcher = updater.dispatcher

# Commands:
def start(bot, update):
    if update.message.chat_id in config.CHATIDLIST:
        bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def where(bot, update):
    if update.message.chat_id in config.CHATIDLIST:
        ip_list = socket.gethostbyname_ex(socket.gethostname())
        bot.send_message(chat_id=update.message.chat_id, text=f'Hostname: {ip_list[0]}')
        for number,ip in enumerate(ip_list[2]):
            msg = f'IP #{number + 1} - {ip}'
            bot.send_message(chat_id=update.message.chat_id, text=msg)

# Handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

where_handler = CommandHandler('where', where)
dispatcher.add_handler(where_handler)

#if __name__ == 'main':
print('IP Bot Started')
updater.start_polling()