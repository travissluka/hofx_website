#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime, timezone

AUTHOR = 'JCSDA'
SITENAME = 'JCSDA Real-Time Observation Monitoring'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'
CURRENTDATE=datetime.now(timezone.utc)

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('JCSDA', 'http://jcsda.org'),
#         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

#DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY=True
ARTICLE_SAVE_AS="{category}/{slug}.html"
CATEGORY_SAVE_AS="{slug}/index.html"

THEME ="./theme"