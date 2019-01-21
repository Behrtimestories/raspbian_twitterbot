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

#Prompt for message
message = input("What's on your mind? ")

#Post it
twitter.update_status(status=message)

#Print Tweet/confirmation
print("Tweeted: {}".format(message))
