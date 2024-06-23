import telegram
from telegram.ext import Updater, CommandHandler
import ccxt

# Токен вашего Telegram бота
TOKEN = '7251746995:AAEa5JkRxY_KDX5pwHiOzvsxtdQfVYH15yo'

# Ключи API от Binance
EXCHANGE_API_KEY = 'YvhJAPSVISNejVQ4mkVbn1rfcum16hyqPryz2jKmLOArThftRTSBHfXJnnLN6rKr'
EXCHANGE_SECRET = 'UEnoFEPFY9kHEM3HVXvv5LKMSI9UgrUGZnvTwL26p1AdbRWR7bwGe2uTuigjNNkI'

# Инициализация биржи (в примере использована Binance)
exchange = ccxt.binance({
    'apiKey': EXCHANGE_API_KEY,
    'secret': EXCHANGE_SECRET,
})

# Обработчик команды /start
def start(update, context):
    update.message.reply_text('Добро пожаловать! Я бот для обмена криптовалюты. Используйте команды /buy и /sell.')

# Обработчик команды /buy
def buy(update, context):
    try:
        # Получаем текущий курс Bitcoin к USDT
        symbol = 'BTC/USDT'
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']

        update.message.reply_text(f'Текущий курс {symbol}: {price} USDT')
    except Exception as e:
        update.message.reply_text(f'Произошла ошибка: {str(e)}')

# Обработчик команды /sell
def sell(update, context):
    update.message.reply_text('Команда /sell ещё не реализована.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("buy", buy))
    dp.add_handler(CommandHandler("sell", sell))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
