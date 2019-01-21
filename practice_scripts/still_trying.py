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
message = "It's hard being a bot! I'm still getting the hang of all these tools!"
twitter.update_status(status=message)
print("Tweeted: {}".format(message))
