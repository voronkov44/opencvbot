import cv2
import numpy as np
import easyocr
import telebot
from telebot import types

bot = telebot.TeleBot("bottoken")

plate = cv2.CascadeClassifier('plate.xml')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}!\nЭто бот, который распознает номерной знак по фотографии, просто отправьте мне фотографию и я напишу его текстом.')



@bot.message_handler(content_types=['photo'])
def handle_image(message):
    photo = message.photo[-1]
    file = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file.file_path)
    file_name = 'downloadimages/image.jpg'
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    img = cv2.imread('downloadimages/image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # насколько крупный номер и насколько много номеров на изображении (исправляем изображение чтобы модель лучше работала)
    plate_text = plate.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

    # устанавливаем рамочку которая выделяет номер
    for (x, y, w, h) in plate_text:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 0), thickness=3)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)

        # Вырезаем область номерного знака из изображения
        plate_roi = gray[y:y + h, x:x + w]

        # Сохраняем область номерного знака в отдельном файле
        cv2.imwrite('redimages/plate_roi.jpeg', plate_roi)


    text = easyocr.Reader(['en'])
    text = text.readtext(plate_roi)
    plate_number = text[0][1] # Получение номера из кортежа
    print(text)

    bot.send_message(message.chat.id, f"Номерной знак:  {plate_number}")

    with open('redimages/plate_roi.jpeg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

bot.polling()