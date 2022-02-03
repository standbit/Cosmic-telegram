from datetime import datetime
import os
from os.path import splitext
from pathlib import Path
from urllib.parse import urlparse, unquote_plus

from dotenv import load_dotenv
import requests


SPACE_DIR = "./cosmos_images/"


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_nasa_epic_images(img_num, token):
    url = "https://api.nasa.gov/EPIC/api/natural"
    payload = {
        "api_key": token
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_json = response.json()
    links = []
    num = 0
    while num < img_num:
        img_name = epic_json[num]["image"]
        img_date = epic_json[num]["date"]
        short_img_date = datetime.fromisoformat(img_date).strftime("%Y/%m/%d")
        base_link = "https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{img}.png"    # Noqa E501
        image_link = base_link.format(date=short_img_date, img=img_name)
        links.append(image_link)
        num += 1
    for image_number, link in enumerate(links):
        image_name = f"nasa_epic{image_number}.png"
        filename = f"{SPACE_DIR}{image_name}"
        download_image(link, filename)


def get_file_extension(link):
    link_path = unquote_plus(urlparse(link).path)
    extension = splitext(link_path)[-1]
    return extension


def fetch_nasa_apod_images(img_num, token):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": token,
        "count": img_num
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    days = response.json()
    links = []
    for day in days:
        if not day["url"]:
            continue
        links.append(day["url"])
    for image_number, link in enumerate(links):
        extension = get_file_extension(link)
        image_name = f"nasa{image_number}{extension}"
        filename = f"{SPACE_DIR}{image_name}"
        download_image(link, filename)


def main():
    load_dotenv()
    token = os.getenv("NASA_TOKEN")
    Path(SPACE_DIR).mkdir(parents=True, exist_ok=True)
    fetch_nasa_apod_images(img_num=15, token=token)
    fetch_nasa_epic_images(img_num=5, token=token)


if __name__ == "__main__":
    main()