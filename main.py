from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from config import TELEGRAM_TOKEN


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет!, Как дела?')


def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, start))
    app.run_polling()


if __name__ == '__main__':
    main()
