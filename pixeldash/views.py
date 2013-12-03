# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.http import HttpResponse

import simplejson as json

from gdata.youtube.service import YouTubeService
from gdata.youtube.service import YouTubeVideoQuery

from twitter_auth import twitter_auth
from serialize import tweet_serialize, video_entry_serialize

class IndexView(TemplateView):
	template_name = "index.html"
	get_services = ('get', )
	
	def _get(self):
		# pega dos 10 primeiros TTs
		api = twitter_auth()		
		items = api.trends_place(23424768)[0]['trends']
		trends = []
		# alterar este contador para rodar o loop 
		count = 1
		for item in items:
			if count <= 0:
				count += 1
				trends.append(item)		
		tweets = []
		for trend in trends:
			tweet = api.search(
				q=trend['name'],
				lang='pt-br',
				count=1,
			)
			for t in tweet:	
				tweets.append(tweet_serialize(t))
		
		#separa os trends que não possuem hashtag
		videos = []
		count = 0
		for item in items:
			if item['name'][0] != "#" and count <= 5:
				count += 1
				query = YouTubeVideoQuery()
				client = YouTubeService()
				query.vq = item['name'].encode('utf-8')
				query.max_results = 1
				entry = client.YouTubeQuery(query).entry[0]
				videos.append(video_entry_serialize(entry))			
		
		
		response = {
			"tweets": tweets,
			"videos": videos
		}
		return HttpResponse(json.dumps(response), 
							content_type="application/json")
	
	def get(self, *args, **kwargs):
		cmd = self.request.GET.get('cmd')
		if cmd and cmd in self.get_services:
			return getattr(self, '_%s' % cmd)()
		
		return super(IndexView, self).get(*args, **kwargs)
