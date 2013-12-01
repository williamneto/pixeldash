# -*- coding: utf-8 -*-
from django.conf.urls import *

from pixeldash.views import IndexView

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view()),
)
