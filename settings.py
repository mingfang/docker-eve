import json
import os

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://user:user@localhost:27017/eve')

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

RENDERERS = [
    'eve.render.JSONRenderer'
]

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

DOMAIN_PATH = os.environ.get('DOMAIN_PATH', 'domain.json')
with open(DOMAIN_PATH, "r") as jsonfile:
    DOMAIN = json.load(jsonfile)

SCHEMA_ENDPOINT = '_schema'
ALLOW_UNKNOWN = True
ENFORCE_IF_MATCH = False
URL_PREFIX = '/'
VERSIONING = True
