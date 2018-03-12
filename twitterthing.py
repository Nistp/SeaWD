#Simple twitter bot in Python

import time, sys, requests, requests_oauthlib
from requests_oauthlib import OAuth1Session

from init_config import init_app
config = init_app('.sewd.conf')

CONSUMER_KEY = config.get('consumer_key')
CONSUMER_SECRET = config.get('consumer_secret')
ACCESS_KEY =  config.get('access_key')
ACCESS_SECRET = config.get('access_secret')

callback_uri = 'https://127.0.0.1/callback'

Request_token_URL = 'https://api.twitter.com/oauth/request_token'
Authorize_URL ='https://api.twitter.com/oauth/authorize'
Access_token_URL =  'https://api.twitter.com/oauth/access_token' 

twitterbot = OAuth1Session(CONSUMER_KEY, client_secret=CONSUMER_SECRET, callback_uri=callback_uri)
#This should be either combined with the parse_autho_response method or be used on its own
fetch_response = twitterbot.fetch_request_token(Request_token_URL)

rok = fetch_response.get('oauth_token')
ros = fetch_response.get('oauth_token_secret')

#gets messed up here with an 89 error code --look up, use fetch response if you can
twitterbot_response = twitterbot.parse_authorization_response(Authorize_URL)
#needed or not? 
verifier = twitterbot_response.get('oauth_verifier')
#needed or not?
access_token_url = 'https://api.twitter.com/oauth/access_token'

twitterbot = OAuth1Session(CONSUMER_KEY,
                         client_secret=CONSUMER_SECRET,
                         resource_owner_key=rok,
                          resource_owner_secret=ros,
                         verifier=verifier)
				
				
twitterbot_tokens = twitterbot.fetch_access_token(access_token_url)

rok = fetch_response.get('oauth_token')
ros = fetch_response.get('oauth_token_secret')

twitterbot = OAuth1Session(CONSUMER_KEY,
                          client_secret=CONSUMER_SECRET,
                          resource_owner_key=rok,
                          resource_owner_secret=ros)
						  

status_url = 'http://api.twitter.com/1.1/statuses/update.json'
new_status = {'status':  'Pythonic Test Tweet!'}
twitterbot.post(status_url, data=new_status)
