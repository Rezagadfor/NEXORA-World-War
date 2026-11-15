
import os
from rubibot import RubiBot

TOKEN = os.getenv("RUBIKA_TOKEN")

if not TOKEN:
    raise RuntimeError("RUBIKA_TOKEN is not set")

bot = RubiBot(TOKEN)

MENU = """
🌍 NEXORA | WORLD WAR

به جهان کشورها خوش آمدید!

🏛️ کشور من
🌐 انتخاب کشور
🏭 زیرساخت و کارخانه‌ها
💰 اقتصاد و منابع
🤝 تجارت جهانی
🪖 مدیریت نیروها
✈️ ناوگان هوایی
🚢 ناوگان دریایی
🔬 تحقیقات و فناوری
🛒 فروشگاه ASIX
👑 مدیریت
"""

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat_id, MENU)

@bot.message_handler()
def menu(message):
    answers = {
        "🏛️ کشور من": "هنوز کشوری انتخاب نکرده‌اید.",
        "🌐 انتخاب کشور": "بخش انتخاب کشور به‌زودی فعال می‌شود.",
        "🏭 زیرساخت و کارخانه‌ها": "بخش زیرساخت‌ها در حال آماده‌سازی است.",
        "💰 اقتصاد و منابع": "بخش اقتصاد در حال آماده‌سازی است.",
        "🤝 تجارت جهانی": "بازار تجارت جهانی به‌زودی فعال می‌شود.",
        "🪖 مدیریت نیروها": "مدیریت نیروها در حال آماده‌سازی است.",
        "✈️ ناوگان هوایی": "بخش ناوگان هوایی در حال آماده‌سازی است.",
        "🚢 ناوگان دریایی": "بخش ناوگان دریایی در حال آماده‌سازی است.",
        "🔬 تحقیقات و فناوری": "مرکز تحقیقات در حال آماده‌سازی است.",
        "🛒 فروشگاه ASIX": "فروشگاه ASIX در حال آماده‌سازی است.",
        "👑 مدیریت": "این بخش مخصوص مدیر اصلی است."
    }

    text = getattr(message, "text", "") or ""
    response = answers.get(text, MENU)
    bot.send_message(message.chat_id, response)

if __name__ == "__main__":
    bot.polling()
