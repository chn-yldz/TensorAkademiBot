import Constants as keys
from telegram.ext import *
import Responses as R
import time
print("TensörAkademi Yapay Zeka Aktifleştiriliyor !!!")
time.sleep(1)



def start_command(update,context):
    update.message.reply_text('TensörAkademiAI Şu Anda Aktif\nYardım İçin /help yazabilirsiniz')

def help_command(update,context):
    update.message.reply_text('Çok Yakında Sizlerleyim Şimdilik Sosyal Medya Hesaplarımıza Göz Atabilirsiniz\nhttps://www.instagram.com/tensorakademi/ veya \nhttps://twitter.com/tensorakademi veya \nhttps://www.youtube.com/channel/UCxq4le0YbomzFkTav6KbSlQ?app=desktop  Adreslerine Bakabilirsiniz\nSağlıklı Günler Dilerim ...')

def handle_message(update,context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    
    update.message.reply_text(response)

def error(update,context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()