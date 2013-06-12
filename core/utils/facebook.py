from django.conf import settings
from django.utils import simplejson
from core.models import User
from core.utils.auth import random_string
import requests


def get_access_token_expire(oauth_code, redirect_uri):
    try:
        resp = requests.get('https://graph.facebook.com/oauth/access_token',
            params={
                'client_id': settings.FACEBOOK_APP_ID,
                'redirect_uri': redirect_uri,
                'client_secret': settings.FACEBOOK_APP_SECRET,
                'code': oauth_code,
            })
        params = resp.text.split('&')
        access_token = params[0].split('=')[1]
        expires = params[1].split('=')[1]
        return access_token, expires
    except:
        return None, None


def get_facebook_user_data(access_token, facebook_id='me'):
    try:
        resp = requests.get('https://graph.facebook.com/' + facebook_id,
            params={
                'access_token': access_token,
            })
        return simplejson.loads(resp.text)
    except:
        return None


def get_facebook_friend_data(access_token, fields='id,name'):
    try:
        resp = requests.get('https://graph.facebook.com/me/friends',
            params={
                'access_token': access_token,
                'fields': fields,
            })
        return simplejson.loads(resp.text)
    except:
        return None


def get_facebook_mutual_friend_data(access_token, friend_id, fields='id,name'):
    try:
        resp = requests.get('https://graph.facebook.com/me/mutualfriends/' + friend_id,
            params={
                'access_token': access_token,
                'fields': fields,
            })
        return simplejson.loads(resp.text)
    except:
        return None


def get_facebook_graph_search_data(access_token, search_term, search_type='user'):
    try:
        resp = requests.get('https://graph.facebook.com/search',
            params={
                'access_token': access_token,
                'q': search_term,
                'type': search_type,
            })
        return simplejson.loads(resp.text)
    except:
        return None


def unbind_facebook_account(user_data):
    try:
        user = User.objects.get(facebook_id=user_data['id'])
        user.facebook_id = None
        user.save()
    except User.DoesNotExist:
        pass


def bind_facebook_account(user, user_data):
    user.facebook_id = user_data['id']
    user.tz_offset = user_data['timezone']
    user.save()


def facebook_connect(user_data):
    try:
        # Logging in with Facebook
        user = User.objects.get(facebook_id=user_data['id'])
        user.tz_offset = user_data['timezone']
        user.save()
    except User.DoesNotExist:
        # Creating new account with Facebook
        user = User()
        user.email = user_data['email']
        user.facebook_id = user_data['id']
        user.tz_offset = user_data['timezone']
        user.set_password(random_string())
        user.save()
    return user
