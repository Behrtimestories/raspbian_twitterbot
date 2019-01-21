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
#message = "Hello, world! I'm excited to start my new job of showing you all weather satellite images!"
#twitter.update_status(status=message)
#print("Tweeted: {}".format(message))
print (twitter.get_account_settings())
