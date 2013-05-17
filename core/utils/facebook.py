import urllib
from django.conf import settings
from django.utils import simplejson
from core.models import User
from core.utils.auth import random_string


def build_token_url(oauth_code, redirect_uri):
    token_url = 'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(
        {
            'client_id': settings.FACEBOOK_APP_ID,
            'redirect_uri': redirect_uri,
            'client_secret': settings.FACEBOOK_APP_SECRET,
            'code': oauth_code,
        }
    )
    return token_url


def get_access_token_expire(token_url):
    try:
        conn = urllib.urlopen(token_url)
        resp = conn.read()
        conn.close()
        params = resp.split('&')
        access_token = params[0].split('=')[1]
        expires = params[1].split('=')[1]
        return access_token, expires
    except:
        return None, None


def get_facebook_user_data(access_token, facebook_id='me'):
    try:
        graph_url = 'https://graph.facebook.com/' + facebook_id + '?' + urllib.urlencode(
            {
                'access_token': access_token,
            }
        )
        conn = urllib.urlopen(graph_url)
        resp = conn.read()
        conn.close()
        return simplejson.loads(resp)
    except:
        return None


def get_facebook_friend_data(access_token, fields='id,name'):
    try:
        graph_url = 'https://graph.facebook.com/me/friends?' + urllib.urlencode(
            {
                'access_token': access_token,
                'fields': fields,
            }
        )
        conn = urllib.urlopen(graph_url)
        resp = conn.read()
        conn.close()
        return simplejson.loads(resp)
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
        user.display_name = '%s %s' % (user_data['first_name'], user_data['last_name'])
        user.set_password(random_string())
        user.save()
    return user
