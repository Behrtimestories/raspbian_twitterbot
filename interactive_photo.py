from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

ask_photo = input("Absolute path to image: ")
message = input("Add a comment? ")
photo = open(ask_photo, 'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=message, media_ids=[response['media_id']])
print("Tweeted: {}".format(message))
