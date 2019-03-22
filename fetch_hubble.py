import os
import requests
import utils



def save_hubble_pic_by_id(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url)
    url_for_save = response.json()['image_files'][-1]['file_url']
    extansion_of_image = utils.get_extansion_of_image(url_for_save)
    path = f'hubble{image_id}.{extansion_of_image}'
    utils.save_picture(url_for_save, path)


def save_hubble_pic_collection(collection_name):
    url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(url)
    for picture in response.json():
        save_hubble_pic_by_id(picture['id'])
