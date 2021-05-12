import logging

from aiogram import executor

from eathalal import bot

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s | %(name)s | %(message)s')

if __name__ == '__main__':
    executor.start_polling(bot.dp)
