#Import the Twython module 
from twython import Twython

#Import the Twitter API keys
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#Create the twitter object out of the seekrits
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#Prompt for photo
ask_photo = input("Absolute path to image: ")

#Prompt for commentary
message = input("Add a comment? ")

#Create the photo object to be posted
photo = open(ask_photo, 'rb')

#Post it
response = twitter.upload_media(media=photo)
twitter.update_status(status=message, media_ids=[response['media_id']])

#Print Tweet/confirmation
print("Tweeted: {}".format(message))
