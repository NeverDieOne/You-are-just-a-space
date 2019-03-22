import requests
import os


def get_extansion_of_image(url):
    return url.split('.')[-1]


def save_picture(url, path):
    os.makedirs('images', exist_ok=True)
    filename = f'images/{path}'
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
