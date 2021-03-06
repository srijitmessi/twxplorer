import sys
import os
import pymongo


# Get settings module
settings = sys.modules[os.environ['FLASK_SETTINGS_MODULE']]

# Connect to mongo database
_conn = pymongo.Connection(
    settings.DATABASES['default']['HOST'],
    int(settings.DATABASES['default']['PORT'])
)
_db = _conn[settings.DATABASES['default']['NAME']]

# Mongo collections
_search = _db['search']
_session = _db['session']
_tweets = _db['tweets']
_url = _db['url']
_list = _db['list']


# Ensure indicies
_search.ensure_index('username')
_search.ensure_index([
    ('username', pymongo.ASCENDING),
    ('query', pymongo.ASCENDING)])

_session.ensure_index('search_id')

_tweets.ensure_index([
    ('session_id', pymongo.ASCENDING),
    ('created_at', pymongo.DESCENDING)])

_url.ensure_index('url')
_url.ensure_index('aka')

_list.ensure_index('username')

