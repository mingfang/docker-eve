import json
import os

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://user:user@localhost:27017/eve')
DOMAIN_PATH = os.environ.get('DOMAIN_PATH', 'domain.json')
with open(DOMAIN_PATH, "r") as jsonfile:
    DOMAIN = json.load(jsonfile)

ALLOW_UNKNOWN = os.environ.get('ALLOW_UNKNOWN', True)
CACHE_CONTROL = os.environ.get('CACHE_CONTROL', 'max-age=20')
CACHE_EXPIRES = os.environ.get('CACHE_EXPIRES', 20)
ENFORCE_IF_MATCH = os.environ.get('ENFORCE_IF_MATCH', False)
ITEM_METHODS = json.loads(os.environ.get('ITEM_METHODS', '["GET", "PATCH", "PUT", "DELETE"]'))
OPLOG = os.environ.get('OPLOG', True)
OPLOG_ENDPOINT = os.environ.get('OPLOG_ENDPOINT', '_oplog')
RESOURCE_METHODS = json.loads(os.environ.get('RESOURCE_METHODS', '["GET", "POST", "DELETE"]'))
RENDERERS = json.loads(os.environ.get('RENDERERS', '["eve.render.JSONRenderer"]'))
SCHEMA_ENDPOINT = os.environ.get('SCHEMA_ENDPOINT', '_schema')
URL_PREFIX = os.environ.get('URL_PREFIX', '/')
VERSIONING = os.environ.get('VERSIONING', True)

