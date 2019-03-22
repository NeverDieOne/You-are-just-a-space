import os
import requests
import utils



def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    for num, picture_url in enumerate(response.json()['links']['flickr_images']):
        utils.save_picture(picture_url, f'sapcex{num}.jpeg')
