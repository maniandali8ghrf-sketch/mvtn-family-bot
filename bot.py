import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = ("8871508590:AAEdUMyU_lPfVAtSf6gZZLlpgCwMgYpMy1k")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎵 Latest Tracks", callback_data="tracks")],
        [InlineKeyboardButton("📢 MVTN News", callback_data="news")],
        [InlineKeyboardButton("👑 Join MVTN FAMILY", callback_data="family")],
        [InlineKeyboardButton("🛍 Store", callback_data="store")],
        [InlineKeyboardButton("📸 Social Media", callback_data="social")],
        [InlineKeyboardButton("🎧 Streaming Platforms", callback_data="stream")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to MVTN FAMILY\n\nOfficial hub for MVTN.",
        reply_markup=reply_markup,
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "tracks": "🎵 Latest Tracks\n\nNo tracks added yet.",
        "news": "📢 MVTN News\n\nNo news yet.",
        "family": "👑 Join MVTN FAMILY\n\nComing Soon.",
        "store": "🛍 Store\n\nComing Soon.",
        "social": "📸 Social Media\n\nInstagram\nTelegram",
        "stream": "🎧 Streaming Platforms\n\nSpotify\nSoundCloud",
    }

    await query.edit_message_text(messages.get(query.data, "Unknown option."))


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()