# -*- coding: utf-8 -*-
from instagram import client

def instagram_auth():
	CONFIG = {
		'client_id': '0ae0309a9cdd4967b59d25aaff06025b',
		'client_secret': 'a4b509f2de89471e98f9a718ec010385',
		'redirect_uri': 'http://127.0.0.1/insta/'
	}

	return client.InstagramAPI(**CONFIG)
