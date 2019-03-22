import requests
import os
from instabot import Bot
from fetch_hubble import save_hubble_pic_collection, save_hubble_pic_by_id
from fetch_spacex import fetch_spacex_last_launch


fetch_spacex_last_launch()
save_hubble_pic_by_id(1)
save_hubble_pic_collection('wallpaper')


bot = Bot()
bot.login(username=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))

for pic in os.listdir('images'):
    bot.upload_photo(f'images/{pic}', caption='Nice pic')
    
