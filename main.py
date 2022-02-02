import os
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote_plus
from os.path import splitext
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_nasa_epic_images(img_num):
    url = "https://api.nasa.gov/EPIC/api/natural"
    token = os.getenv("NASA_TOKEN")
    payload = {
        "api_key": token
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_json = response.json()
    links = []
    num = 0
    while num < img_num:
        image_name = epic_json[num]["image"]
        image_date = epic_json[num]["date"]
        cutted_image_date = datetime.fromisoformat(image_date).strftime("%Y/%m/%d")
        image_link = "https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{img}.png".format(date=cutted_image_date, img=image_name)
        links.append(image_link)
        num += 1
    space_dir = "./nasa_epic_images/"
    Path(space_dir).mkdir(parents=True, exist_ok=True)
    for image_number, link in enumerate(links):
            image_name = f"nasa_epic{image_number}.png"
            filename = f"{space_dir}{image_name}"
            download_image(link, filename)


def fetch_spacex_images(flight_num):
    space_dir = "./spacex_images/"
    Path(space_dir).mkdir(parents=True, exist_ok=True)
    url = "https://api.spacexdata.com/v3/launches/{flight_number}"
    response = requests.get(url.format(flight_number=flight_num))
    response.raise_for_status()
    links = response.json()["links"]["flickr_images"]
    for image_number, link in enumerate(links):
            image_name = f"spacex{image_number}.jpg"
            filename = f"{space_dir}{image_name}"
            download_image(link, filename)


def get_file_extension(link):
    link_path = unquote_plus(urlparse(link).path)
    extension = splitext(link_path)[-1]
    return extension


def fetch_nasa_apod_images(img_num):
    space_dir = "./nasa_apod_images/"
    Path(space_dir).mkdir(parents=True, exist_ok=True)
    url = "https://api.nasa.gov/planetary/apod"
    token = os.getenv("NASA_TOKEN")
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
        filename = f"{space_dir}{image_name}"
        download_image(link, filename)


def main():
    load_dotenv()
    try:
        fetch_nasa_epic_images(5)
        fetch_nasa_apod_images(5)
        fetch_spacex_images(16)
    except requests.exceptions.HTTPError as err:
            print("General Error, incorrect link\n", str(err))
    except requests.ConnectionError as err:
            print("Connection Error. Check Internet connection.\n", str(err))


if __name__ == "__main__":
    main()