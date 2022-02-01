import requests
from pathlib import Path


SPACE_DIR = "space_photos/"


def get_picture():
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    response = requests.get(url)
    response.raise_for_status()
    return response


def save_picture(response):
    filename = "hubble.jpeg"
    with open(SPACE_DIR + filename, 'wb') as file:
        file.write(response.content)


def main():
    Path("./space_photos/").mkdir(parents=True, exist_ok=True)
    try:
        response = get_picture()
    except requests.exceptions.HTTPError as err:
            print("General Error, incorrect link\n", str(err))
    except requests.ConnectionError as err:
            print("Connection Error. Check Internet connection.\n", str(err))
    save_picture(response)


if __name__ == "__main__":
    main()