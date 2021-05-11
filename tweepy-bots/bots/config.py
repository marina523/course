# tweepy-bots//config.py
import tweepy
import logging
import os

logger = logging.getLogger()
CONSUMER_KEY = 'qmIYEcpg6dAqekRXb84VMc3rY'
CONSUMER_SECRET = 'ZtBRdRF4EYrrXGpzHqNIf8nSgRkAQRNBo7m63s4qD4iuUWojZ7'
ACCESS_TOKEN = '1390884054317342721-PRTi9HyxxrKPkyhJmcAkQPfgPg6H8n'
ACCESS_TOKEN_SECRET = 'ywk1IxBAnCi4NfWJ7zAQWuwG6GyUQa7Dy6yRbH1WeGAvC'

def create_api():
    consumer_key = os.getenv(CONSUMER_KEY)
    consumer_secret = os.getenv(CONSUMER_SECRET)
    access_token = os.getenv(ACCESS_TOKEN)
    access_token_secret = os.getenv(ACCESS_TOKEN_SECRET)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api