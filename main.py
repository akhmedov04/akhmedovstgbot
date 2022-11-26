import os

from aiogram import *
from pytube import YouTube

bot = Bot("5885229538:AAErgF3u22W9B8ohN-UmUQ--Eigdg84jQGc")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id , "Привет, я могу скачать видео с YouTube\n"
                                     "Отправьте мне ссылку!")


@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == "https://youtu.be/" or "https://youtube.com/" :
        await bot.send_message(chat_id, "Начинаю загрузку видео!")
        await download_youtube_video(url, message, bot)
    else:
        await bot.send_message(chat_id, ":(")


async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_lowest_resolution().download(f"{message.chat.id}", f"{message.chat.id}_{yt.title}")
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", "rb") as video:
        await bot.send_video(message.chat.id, video, caption="*Готово!*", parse_mode="Markdown")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")


if __name__ == "__main__":
    executor.start_polling(dp)
