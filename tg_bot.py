from email.policy import default
import os
import random
import time

from dotenv import load_dotenv
import telegram


SPACE_DIR = "./cosmos_images/"


def main():
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")
    sleep_time = int(os.getenv("SLEEP_TIME"))
    tg_chat_id = os.getenv("TG_CHAT_ID")
    bot = telegram.Bot(token=tg_token)
    cosmos_images = os.listdir(SPACE_DIR)
    while True:
        bot.send_photo(
            chat_id=tg_chat_id,
            photo=open("{dir}/{image}".format(
                dir=SPACE_DIR,
                image=random.choice(cosmos_images)),
                "rb")
                )
        time.sleep(sleep_time, default=15)


if __name__ == "__main__":
    main()
