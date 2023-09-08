import logging
from typing import Final
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, ConversationHandler, \
    CallbackQueryHandler
import random

BOT_TOKEN: Final = "Token"
Bot_USERNAME: Final = "@HelloBoy2023bot"
DEV_ID = "ID"

logging.basicConfig(format='%(levelname)s - (%(asctime)s) - %(message)s - (Line: %(lineno)d) - [%(filename)s]',
                    datefmt='%H:%M:%S',
                    encoding='utf-8',
                    level=logging.WARNING)

logger = logging.getLogger(__name__)

# </start> --> starting the bot
# </play>  --> choosing truth or courage
# </help> --> helping to use bot
# </truth> --> choosing truth question
# </courage> --> choosing courage question
# </exit>   --> ending the game
truth_items = [
    "آخرین بار که دروغ گفتی درباره چی بود؟",
    "بهترین روز زندگیت چه روزی بوده؟",
    "اگر می‌تونستی نامرئی بشی چکار می‌کردی؟",
    "آخرین چیزی که امروز روی گوشی جستجو کردی چی بوده؟",
    "یک ویژگی بد از خودت بگو؟‌",
    "چه کسی رو پنهانی دوست داری؟",
    "بدترین شوخی که با کسی داشته ای چه بوده است؟",
    "اسم کسی را بگو که وانمود می کنی دوستش داری اما در واقع چشم دیدنش را نداری",
    "به کدام عضو بدن خودت علاقه داری و از کدام متنفر هستی؟",
    "خجالت آورترین خاطره کودکی ات چیست؟",
    "اگر غول چراغ جادو داشته باشی سه آرزویت چیست؟",
    "آیا با دریافت 5 میلیارد تومان حاضر هستی از همسرت جدا شوی؟",
    " آیا تا به حال تحقیر شده ای؟ داستانش را تعریف کن",
    "احمقانه ترین اعتیاد یا وابستگی که داری چیست؟",
    "به من چیزی بگو که نمی خواهی بدانم",
    " اگر مطمئن باشی هیچ وقت زندانی نمی شوی دوست داری چه کسی را بکشی؟"
]
courage_items = [
    "یک پیام به اولین شخصی که در تلگرام آنلاین است بفرست",
    "یک حرکت رقص خنده دار انجام بده",
    "اولین کلمه ای که به ذهنت می رسد را فریاد بزن",
    "یک دقیقه کامل پلک نزن",
    "یک قطعه یخ در شلوار خود قرار بده و صبر کن تا آب شود",
    "کاغذ شکلات را تنها با استفاده از دهان خود باز کن",
    "دست خود را تا آرنج داخل سطل زباله فرو ببر",
    "اجازه بده گروه به مدت یک دقیقه به داخل تلفن همراهت سرک بکشند",
    "نام خود را با زبان روی زمین بنویس",
    "یک عدد پیاز خام بخور و گریه نکن",
    "برای یک ربع در خیابان راه برو و بلند بلند با خودت صحبت کن",
    "چهار تکه از لباس هایت را با شرکت کننده سمت راستت عوض کن",
    "یک عدد شکلات را روی ترشی بگذار و بخور",
    "با تمام لباس هایی که به تن داری دوش بگیر",
    "به یکی از شرکت کنندگان اجازه بده کلمه ای روی پیشانی ات بنویسد و تا آخر بازی آن را پاک نکن",
    "به بالای پشت بام برو و فریاد بزن من بچه سر راهی هستم"
]


async def start_Handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("user %s started the bot.", update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="سلام،خوبي؟به ربات جرئت حقیقت خوش اومدي."
             "\nفقط كافيه برای شروع بازی play/ رو بزنی."
             "\n.امیدوارم از بازی لذت ببری❤️",

        reply_to_message_id=update.effective_message.id
    )


async def help_Handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("user %s needs help.", update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.effective_message.id,
        text="""Welcome to HelloBoy bot:
        /start --> شروع ربات
        /truth --> انتخاب حقیقت
        /courage --> انتخاب جرئت
        /play --> شروع بازی
        /help --> کمک برای آشنایی با ویزگی های بات
        /exit --> برای پایان بازی 
        لحظات خوبی را برای شما آرزومندم"""
    )


async def play_Handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("user %s wants to play.", update.effective_user.id)
    reply_keyboard = [
        ["حقیقت", "جرئت"],
        ["Help", "پایان"],
    ]
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="خب الان از بین جرئت یا حقیقت یکدوم رو انتخاب کن دوست من"
             "\n\n🔔توجه:اگه نیاز به کمک داری توضیه میکنم بهت از دستور help/ حتما استفاده کنی.🔔",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="جرئت یا حقبقت ؟",
        ),
        reply_to_message_id=update.effective_message.id,
    )


async def truth_Handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("user %s choosed truth.", update.effective_user.id)
    truth_list = truth_items
    truth = random.choice(truth_list)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"سوال حقیقت: {truth}",
        reply_to_message_id=update.effective_message.id
    )


async def courage_Handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("user %s choosed courage.", update.effective_user.id)
    courage_list = courage_items
    courage = random.choice(courage_list)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"سوال جرئت: {courage}",
        reply_to_message_id=update.effective_message.id
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()
    if 'جرئت' in message_text:
        await courage_Handler(update, context)
    elif 'حقیقت' in message_text:
        await truth_Handler(update, context)
    elif 'help' in message_text:
        await help_Handler(update, context)
    elif 'پایان' in message_text:
        await cancel_Handler(update, context)


async def cancel_Handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("user %s cancel.", update.effective_user.id)
    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text="خداحافظ.امیدوارم بازی جرئت حقیقت برای شما جالب بوده باشد"
             "\nبه امید دیدار مجدد شما❤️",
        reply_markup=ReplyKeyboardRemove(),
        reply_to_message_id=update.effective_message.id,
    )
    return ConversationHandler.END


async def error_Handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error("error %s update %s", context.error, update)


if __name__ == '__main__':
    logger.info("starting bot ...")
    bot = ApplicationBuilder().token(BOT_TOKEN).build()
    bot.add_handler(CommandHandler("start", start_Handler))
    bot.add_handler(CommandHandler("help", help_Handler))
    bot.add_handler(CommandHandler("play", play_Handler))
    bot.add_handler(CommandHandler("truth", truth_Handler))
    bot.add_handler(CommandHandler("courage", courage_Handler))
    bot.add_handler(CommandHandler("exit", cancel_Handler))
    bot.add_handler(MessageHandler(filters.Text and ~filters.COMMAND, handle_message))
    bot.add_error_handler(error_Handler)
    logger.info("start polling ...")
    bot.run_polling()
