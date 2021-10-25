import tweepy
import schedule
import time

# Importa as keys em config.py
from config import *

# Autentizar
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Coisa de API
api = tweepy.API(auth)


def job():
    api.update_with_media(filename="bot1imgsol.jpg", status="Bom dia, @jadexxw! 🌸⛅\n\nCom você ao meu lado sei que todos os dias podem ser perfeitos. Tenha um ótimo dia!")
    return

schedule.every().day.at("15:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
