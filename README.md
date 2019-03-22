#Космический Инстаграм

Скрипт скачивает фото с API SpaceX и Hubble и постит их в инстаграм.

##Как установить
Python 3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей.

`pip install -r requirements.txt`

##Инструкция
Для получения справки используйте `python main.py -h` или `python main.py --help`

####Чтобы скачать картинки с последнего запуска SpaceX используйте:
`python main.py -s` или `python main.py --space`

####Чтобы скачать картинки с API Hubble используйте:
* Для скачивания картинки по ID:
`python main.py -hi` или `python main.py --hubble_id`
* Для скачивания картинки по имени коллекции:
`python main.py -hc` или `python main.py --hubble_collection`

####Чтобы запостить картинки в Instagram используйте:
`python main.py -i` или `python main.py -inst` 


##Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/).
