import json
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

FILE = "addresses.json"

# load addresses
def load_addresses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return [
            "0xf466729D760e8AF856a6535C50a30847fdB1107B",
            "nafiz_002",
            "0x6471f7AAcA225dB0e560047FF075a9E02ECe0882",
            "0x8A806A0eC49c60246aD5427eDBA515E36a487067",
            "nafiz_005"
        ]

# save addresses
def save_addresses(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

addresses = load_addresses()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global addresses

    if len(addresses) == 0:
        await update.message.reply_text("No address left!")
        return

    address = random.choice(addresses)
    addresses.remove(address)
    save_addresses(addresses)

    await update.message.reply_text(address)

app = ApplicationBuilder().token("8777596178:AAH6la7x2a8jDbvH8Yqk52Qdx0BC9f6tZeY").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
