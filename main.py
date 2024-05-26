import cv2
import os
import numpy as np
import easyocr
import telebot
from telebot import types

bot = telebot.TeleBot("bottoken")

plate = cv2.CascadeClassifier('plate.xml')

proccessing_message = None

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}!\nЭто бот, который распознает номерной знак по фотографии, просто отправьте мне фотографию и я напишу его текстом.')



@bot.message_handler(content_types=['photo'])
def handle_image(message):
    global processing_message
    processing_message = bot.send_message(message.chat.id, "Обрабатываем ваш вопрос...")

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
    if len(plate_text) == 0:
        bot.send_message(message.chat.id, "Не удалось найти номерной знак на этой фотографии.")
        bot.delete_message(message.chat.id, processing_message.message_id)
    else:
        for (x, y, w, h) in plate_text:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 0), thickness=3)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)

            # Вырезаем область номерного знака из изображения
            plate_roi = gray[y:y + h, x:x + w]

            # Сохраняем область номерного знака в отдельном файле
            cv2.imwrite('redimages/plate_roi.jpeg', plate_roi)

            text = easyocr.Reader(['ru'])
            text = text.readtext(plate_roi)

            if text:
                plate_number = text[0][1].upper()  # Получение номера из кортежа
                plate_number = plate_number.replace('[', '').replace(']', '').replace('/', '').replace('₽', 'Р').replace(':', '').replace(';', '').replace('{', '').replace('}', '').replace('`', '').replace(' ', '') # Удаление символов [ и ]
                # 1массив
                for i in range(0, 1):
                    if '0' in plate_number[:1]:
                        plate_number = plate_number[:1].replace('0', 'O') + plate_number[1:4] + plate_number[4:]
                    elif '1' in plate_number[:1]:
                        plate_number = plate_number[:1].replace('1', 'Т') + plate_number[1:4] + plate_number[4:]
                #2 массив
                for i in range(1, 4):
                    if 'О' in plate_number[1:4]:
                        plate_number = plate_number[:1] + plate_number[1:4].replace('О', '0') + plate_number[4:6] + plate_number[6:]
                    elif 'Б' in plate_number[1:4]:
                        plate_number = plate_number[:1] + plate_number[1:4].replace('Б', '5') + plate_number[4:6] + plate_number[6:]
                #3массив
                for i in range(4, 6):
                    if '0' in plate_number[4:6]:
                        plate_number = plate_number[:1] + plate_number[1:4] + plate_number[4:6].replace('0', 'О') + plate_number[6:]
                    elif '1' in plate_number[4:6]:
                        plate_number = plate_number[:1] + plate_number[1:4] + plate_number[4:6].replace('1', 'T') + plate_number[6:]
                for i in range(6, 10):
                    if 'Б' in plate_number[6:]:
                        plate_number = plate_number[:1] + plate_number[1:4] + plate_number[4:6] + plate_number[6:].replace('Б', '5')
                output_array = [plate_number[0], plate_number[1:4], plate_number[4:6], plate_number[6:]]
                output_array = ''.join(output_array)
                print(text)
                print(output_array)

                bot.delete_message(message.chat.id, processing_message.message_id)
                bot.send_message(message.chat.id, f"Номерной знак:  {output_array}")

            with open('redimages/plate_roi.jpeg', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)

    # Удаление временных файлов
    if os.path.exists('downloadimages/image.jpg'):
        os.remove('downloadimages/image.jpg')
    if os.path.exists('redimages/plate_roi.jpeg'):
        os.remove('redimages/plate_roi.jpeg')

bot.polling()