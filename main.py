from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from config import TOKEN


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет!')


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, start))
    app.run_polling()


if __name__ == '__main__':
    main()
