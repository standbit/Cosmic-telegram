from pathlib import Path

import requests


SPACE_DIR = "./cosmos_images/"


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_images(flight_num):
    url = "https://api.spacexdata.com/v3/launches/{flight_number}"
    response = requests.get(url.format(flight_number=flight_num))
    response.raise_for_status()
    links = response.json()["links"]["flickr_images"]
    for image_number, link in enumerate(links):
        image_name = f"spacex{image_number}.jpg"
        filename = f"{SPACE_DIR}{image_name}"
        download_image(link, filename)


def main():
    Path(SPACE_DIR).mkdir(parents=True, exist_ok=True)
    try:
        fetch_spacex_images(flight_num=33)
    except requests.exceptions.HTTPError as err:
        print("General Error, incorrect link\n", str(err))
    except requests.ConnectionError as err:
        print("Connection Error. Check Internet connection.\n", str(err))


if __name__ == "__main__":
    main()
