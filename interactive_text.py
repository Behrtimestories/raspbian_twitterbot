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
#Add some additional tags?
while True:
    tagquestion = input('Would you like to add some tags? \n')
    if tagquestion == '' or not tagquestion[0].lower() in ['y','n']:print('Please answer with yes or no!')
                    #        else:break
    if tagquestion[0].lower() == 'y': 
        taglist = input("No, that's fine. Hash... just hashtag it.")
        message = message + taglist
        break
    if tagquestion[0].lower() == 'n':
        print("Carrying on, then")
        break

#Post it
twitter.update_status(status=message)

#Print Tweet/confirmation
print("Tweeted: {}".format(message))
