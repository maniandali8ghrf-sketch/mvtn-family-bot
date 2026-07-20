from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎵 Latest Tracks", callback_data="tracks")],
        [InlineKeyboardButton("📢 MVTN News", callback_data="news")],
        [InlineKeyboardButton("👑 Join MVTN FAMILY", callback_data="family")],
        [InlineKeyboardButton("🛍 Store", callback_data="store")],
        [InlineKeyboardButton("📸 Social Media", callback_data="social")],
        [InlineKeyboardButton("🎧 Streaming Platforms", callback_data="stream")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to MVTN FAMILY\n\nOfficial hub for MVTN.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "tracks":
        await query.edit_message_text("🎵 Latest Tracks\n\nهنوز آهنگی اضافه نشده.")
    elif query.data == "news":
        await query.edit_message_text("📢 MVTN News\n\nفعلاً خبری منتشر نشده.")
    elif query.data == "family":
        await query.edit_message_text("👑 Join MVTN FAMILY\n\nبه زودی.")
    elif query.data == "store":
        await query.edit_message_text("🛍 Store\n\nبه زودی.")
    elif query.data == "social":
        await query.edit_message_text("📸 Social Media\n\nInstagram\nTelegram")
    elif query.data == "stream":
        await query.edit_message_text("🎧 Spotify / SoundCloud\n\nComing Soon.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()