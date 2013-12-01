import tweepy

def twitter_auth():
	consumer_key="5bzwN5DvamxYgjo7UQsJjQ"
	consumer_secret="blychZKXcaRimBvW4ZuCCFU3eEbWcVwcgOcUJezB4"
	access_token="158044487-QWNnmfiYKxvSlLMuB9qQPApqHz2GMxaq6LtLpzGG"
	access_token_secret="jdq64zMhx5nJWMPeHL9LZkYX6nuAvgm7RBYXBWPwUXE2l"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)

