# **Установка Telegram-бота, который считывает номерной знак и присылает его пользователю.**
Отчет проекта находится [тут.](https://docs.google.com/document/d/1XFECV7O_S8rzrJIuWFY1LIbDuOBEEY0uB-2Ud7cqo00/edit?usp=sharing)
## **Установка**
Для клонирования репозитория необходимо перейти в любую удобную директорию и выполнить команду в терминале:

```no-highlight
git clone https://github.com/voronkov44/opencvbot.git
```

Затем необходимо перейти в корневую директорию проекта:

```no-highlight
cd opencvbot
```

## **Использование**

Для сборки и запуска проекта необходимо выполнить следующие шаги:

**1.** Открываем проект в любом удобном IDE, я буду открывать проект в PyCharm от компании JetBrains.
![image](https://github.com/voronkov44/opencvbot/assets/123954369/a8f50386-8e12-4912-b577-c3e1829fcb91)

Для установки IDE PyCharm смотрите [зависимости.](https://github.com/voronkov44/opencvbot/tree/readme_branch?tab=readme-ov-file#%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8) 

**2.** После открытия проекта нам необходимо скачать нужные нам библиотеки через терминал в самом IDE.
 
**2.1** Устанавливаем библиотеку opencv. 

```no-highlight
pip install opencv-python
```
![image](https://github.com/voronkov44/opencvbot/assets/123954369/02cb8519-340d-4e99-b958-6f51eff96f10)

**2.2** Устанавливаем библиотеку easyOCR.

```no-highlight
pip install easyocr
```
![image](https://github.com/voronkov44/opencvbot/assets/123954369/2375fb29-4997-4f14-a898-ca684a541d2e)


**2.3** Устанавливаем библиотеку telebot.

```no-highlight
pip install telebot
```
![image](https://github.com/voronkov44/opencvbot/assets/123954369/e4d79822-fb4e-41e7-b8be-cbad3d30a5d5)


**3.** После установки библиотек нам необходимо создать телеграм бота.

Как создать телеграм бота можете найти [тут.](https://www.google.com/search?q=%D0%BA%D0%B0%D0%BA+%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C+%D1%82%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC+%D0%B1%D0%BE%D1%82%D0%B0&oq=%D0%BA%D0%B0%D0%BA+%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C+%D1%82%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC+%D0%B1%D0%BE%D1%82%D0%B0&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyDAgBEAAYFBiHAhiABDIMCAIQABgUGIcCGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAEqAIAsAIA&sourceid=chrome&ie=UTF-8#ip=1)

**4.** После создания телеграм бота, необходимо заменить bottoken в коде на токен вашего бота.

**5.** После проделанных шагов можете использовать телеграм бота

Пример работы телеграм бота:


![image](https://github.com/voronkov44/opencvbot/assets/123954369/5677d6ca-4cf2-48ab-af65-58c6c5bf45fd)


## **Зависимости**

Установка IDE [PyCharm.](https://www.jetbrains.com/pycharm/)

## **Библиотеки**

[Opencv:](https://habr.com/ru/articles/519454/)
OpenCV (англ. open source computer vision library) — библиотека алгоритмов компьютерного зрения, обработки изображений и численных алгоритмов общего назначения с открытым кодом. Реализована на Си/C++, также разрабатывается для Python, Java, Ruby, Matlab, Lua и других языков.

[EasyOCR:](https://habr.com/ru/articles/573030/)
EasyOCR это пакет для Python, который предоставляет готовый к использованию механизм OCR и поддерживает 80+ языков. EasyOCR легко устанавливается и очень прост в использовании.

[Telebot:](https://habr.com/ru/articles/580408/)
Библиотека Telebot для телеграм ботов на Python предоставляет ряд основных функций: TeleBot(token) – конструктор класса, который принимает токен вашего бота. send_message(chat_id, text) – отправляет сообщение пользователю с указанным chatid .
  











