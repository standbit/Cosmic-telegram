import requests

import fetch_nasa
import fetch_spacex
import tg_bot


def main():
    try:
        fetch_spacex.main()
        fetch_nasa.main()
    except requests.exceptions.HTTPError as err:
        print("General Error, incorrect link\n", str(err))
    except requests.ConnectionError as err:
        print("Connection Error. Check Internet connection.\n", str(err))
    tg_bot.main()


if __name__ == "__main__":
    main()
