import requests
from pathlib import Path


def download_picture(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def get_spacex_links():
    url = "https://api.spacexdata.com/v3/launches/{flight_number}"
    response = requests.get(url.format(flight_number=33))
    response.raise_for_status()
    links = response.json()["links"]["flickr_images"]
    return links


def main():
    space_dir = "./images/"
    Path(space_dir).mkdir(parents=True, exist_ok=True)
    try:
        links = get_spacex_links()
        for image_number, link in enumerate(links):
            image_name = f"spacex{image_number}.jpg"
            filename = space_dir + image_name
            download_picture(link, filename)
    except requests.exceptions.HTTPError as err:
            print("General Error, incorrect link\n", str(err))
    except requests.ConnectionError as err:
            print("Connection Error. Check Internet connection.\n", str(err))
    print(get_spacex_links())

if __name__ == "__main__":
    main()