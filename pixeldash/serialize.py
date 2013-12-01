def tweet_serialize(tweet):
	return {
		'id': tweet.id,
		'text': tweet.text,
		'user': tweet.user.name		
	}

def video_entry_serialize(entry):
	return {
		'title': entry.title.text,
		'link': entry.link[0].href
	}
	
