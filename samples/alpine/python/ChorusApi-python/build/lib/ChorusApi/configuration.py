from __future__ import absolute_import
import base64
import urllib3

def get_api_key_with_prefix(key):
    global api_key
    global api_key_prefix

    if api_key.get(key) and api_key_prefix.get(key):
      return api_key_prefix[key] + ' ' + api_key[key]
    elif api_key.get(key):
      return api_key[key]

def get_basic_auth_token():
    global username
    global password

    return urllib3.util.make_headers(basic_auth=username + ':' + password).get('authorization')

def auth_settings():
    return { 
               'key': {
                   'type': 'api_key',
                   'in': 'query',
                   'key': 'session_id',
                   'value': get_api_key_with_prefix('session_id')
               },
             
           }

# Default Base url
host = "https://10.0.0.204:8443/"

# Default api client
api_client = None
             
# Authentication settings

api_key = {}
api_key_prefix = {}
username = ''
password = ''


