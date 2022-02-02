import os
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote_plus
from os.path import splitext
from dotenv import load_dotenv


def download_picture(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def get_nasa_image_link():
    url = "https://api.nasa.gov/planetary/apod"
    token = os.getenv("NASA_TOKEN")
    payload = {
        "api_key": token
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    link = response.json()["url"]
    return link


def fetch_spacex_launch(flight_number):
    space_dir = "./spacex_images/"
    Path(space_dir).mkdir(parents=True, exist_ok=True)
    url = "https://api.spacexdata.com/v3/launches/{flight_number}"
    response = requests.get(url.format(flight_number=flight_number))
    response.raise_for_status()
    links = response.json()["links"]["flickr_images"]
    for image_number, link in enumerate(links):
            image_name = f"spacex{image_number}.jpg"
            filename = space_dir + image_name
            download_picture(link, filename)


def get_file_extension(link):
    link_path = unquote_plus(urlparse(link).path)
    extension = splitext(link_path)[-1]
    return extension


def main():
    load_dotenv()
    try:
        # fetch_spacex_launch(25)
        nasa_link = get_nasa_image_link()
        print(get_file_extension(nasa_link))
    except requests.exceptions.HTTPError as err:
            print("General Error, incorrect link\n", str(err))
    except requests.ConnectionError as err:
            print("Connection Error. Check Internet connection.\n", str(err))


if __name__ == "__main__":
    main()