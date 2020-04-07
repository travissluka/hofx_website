#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime, timezone

AUTHOR = 'JCSDA'
SITENAME = 'JCSDA Real-Time Observation Monitoring'
SITEURL = ''
TIMEZONE = 'UTC'
CURRENTDATE=datetime.now(timezone.utc)
PATH = 'content'
DEFAULT_LANG = 'en'
THEME ="./theme"
WELCOME_DESCRIPTION="""
TODO: someone insert a description of what this website is (A set of prety plots to make Tom happy??). 
Insert description at /pelicanconf.py -> WELCOME_DESCRIPTION"
"""

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
PAGE_PATHS=['pages']
DEFAULT_DATE='fs'
#STATIC_PATHS=['images']

ARTICLE_SAVE_AS="{category}/{slug}.html"
CATEGORY_SAVE_AS="{slug}/index.html"
PAGE_SAVE_AS="{category}/slug.html"


# diabled automatically generated pages
IGNORE_FILES=['index.rst']
ARCHIVES_SAVE_AS=''
AUTHOR_SAVE_AS=''
AUTHORS_SAVE_AS=''
CATEGORIES_SAVE_AS=''
TAGS_SAVE_AS=''

