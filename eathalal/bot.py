import os

from aiogram import Bot, Dispatcher, types

from eathalal.animal_data import animals

token = os.environ.get('BOT_TOKEN').strip()
if not token:
    raise EnvironmentError("You must provide `BOT_TOKEN` environment variable.")

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer(
        'Ас-саляму \'алейкум ва рахмату Ллахи ва баракатух!\n\n'
        'Просто отправьте мне название животного, только без ошибок. 😅'
    )


@dp.message_handler()
async def on_query(message: types.Message):
    results_count = 0

    for animal in animals.search(message.text):
        results_count += 1

        if animal.is_halal is True:
            rule_text = '<b>да</b>. ✅'
        elif animal.is_halal is False:
            rule_text = '<b>нет</b>. ❌'
        else:  # can be None
            rule_text = '<b>разногласия.</b> ❓'

        await message.reply((
            f"Животное: <b>{animal.name}</b>.\n"
            f"Дозволено в пищу: {rule_text}\n"
            f"Комментарий: <i>{animal.comment.rstrip('.')}</i>."
        ), parse_mode='HTML')

        if results_count >= 3:
            break

    if results_count == 0:
        await message.reply('Ничего не найдено...')
