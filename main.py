import requests
import os
from instabot import Bot
from fetch_hubble import save_hubble_pic_collection, save_hubble_pic_by_id
from fetch_spacex import fetch_spacex_last_launch
import argparse


parser = argparse.ArgumentParser(description='Скрипт скачивает картинки с API SpaceX/Hubble в папку images или постит картинки из папки images')
parser.add_argument('-s', '--space', action='store_true', help='Скачивает с API SpaceX')
parser.add_argument('-hi', '--hubble_id', help='ID картинки для скачивания с API Hubble', type=int)
parser.add_argument('-hc', '--hubble_collection', help='Имя коллекции для скачивания с API Hubble')
parser.add_argument('-i', '--inst', action='store_true', help='Постит картинки в Instagram')

args = parser.parse_args()

if args.space:
  fetch_spacex_last_launch()

if args.hubble_id:
  save_hubble_pic_by_id(args.hubble_id)

if args.hubble_collection:
  save_hubble_pic_collection(args.hubble_collection)

if args.inst:
  bot = Bot()
  bot.login(username=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))

  for pic in os.listdir('images'):
      bot.upload_photo(f'images/{pic}')

else:
  print('Error\nВведите хотя бы 1 аргумент')
    
