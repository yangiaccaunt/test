import re
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from telegraph import Telegraph
import segno
from io import BytesIO

main_router: Router = Router()


telegraph = Telegraph()

def save_qr(word):
    qrcode = segno.make_qr(word)
    img = BytesIO()
    qrcode.save(img, kind='png', scale=10)
    img.seek(0)
    response = telegraph.upload_file(img)
    link = 'https://telegra.ph' + response[0]['src']
    return link

@main_router.message(Command('start'))
async def start(message: Message):
    await message.answer("Iltimos matn yuboring ")
    
@main_router.message()
async def url_to_qr(message: Message):

    link = save_qr(message.text)
    await message.reply(link)