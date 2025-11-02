

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

TOKEN = "7671988428:AAGW72byUpNshBql_d9pWMNgB-HW_NvX41I"  

START, ASK_NAME, ASK_AGE, SHOW_RESULT = range(4)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["Заполнить анкету", "Выйти"]]
    await update.message.reply_text(
        "Привет! Хочешь рассказать о себе?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return START

async def ask_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "Выйти":
        await update.message.reply_text("Всего доброго!", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    await update.message.reply_text("Введите своё имя:", reply_markup=ReplyKeyboardRemove())
    return ASK_NAME

async def ask_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Введите свой возраст:")
    return ASK_AGE

async def show_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["age"] = update.message.text
    name = context.user_data.get("name", "неизвестно")
    age = context.user_data.get("age", "не указано")
    await update.message.reply_text(f"Анкета заполнена!\nИмя: {name}\nВозраст: {age}")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Опрос прерван.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [
                MessageHandler(filters.Regex("^Заполнить анкету$"), ask_name),
                MessageHandler(filters.Regex("^Выйти$"), cancel)
            ],
            ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_age)],
            ASK_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, show_result)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
