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

photo = open('/home/pi/Pictures/sleepy_pye.jpg', 'rb')
response = twitter.upload_media(media=photo)
message = "She's older now, and quite the elegant grand dame"
twitter.update_status(status=message, media_ids=[response['media_id']])
print("Tweeted: {}".format(message))
