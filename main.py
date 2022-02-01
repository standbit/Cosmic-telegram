import requests
from pathlib import Path


def download_picture(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    space_dir = "./images/"
    Path(space_dir).mkdir(parents=True, exist_ok=True)
    image_name = "hubble.jpeg"
    filename = space_dir + image_name 
    link = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    try:
        download_picture(link, filename)
    except requests.exceptions.HTTPError as err:
            print("General Error, incorrect link\n", str(err))
    except requests.ConnectionError as err:
            print("Connection Error. Check Internet connection.\n", str(err))


if __name__ == "__main__":
    main()