import urllib
from django.conf import settings
from core.utilities import get_domain, random_string, instant_login
from core.models import User
from django.utils import simplejson
from django.http import HttpResponsePermanentRedirect


class FacebookMiddleware(object):

    '''def build_token_url(self, oauth_code, redirect_uri):
        token_url = 'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(
            {
                'client_id': settings.FACEBOOK_APP_ID,
                'redirect_uri': redirect_uri,
                'client_secret': settings.FACEBOOK_APP_SECRET,
                'code': oauth_code,
            }
        )
        return token_url

    def get_access_token_expire(self, token_url):
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

    def get_current_user_data(self, access_token):
        try:
            graph_url = 'https://graph.facebook.com/me?' + urllib.urlencode(
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

    def unbind_facebook_account(self, user_data):
        try:
            user = User.objects.get(facebook_id=user_data['id'])
            user.facebook_id = None
            user.save()
        except User.DoesNotExist:
            pass

    def bind_facebook_account(self, user, user_data):
        user.facebook_id = user_data['id']
        user.tz_offset = user_data['timezone']
        user.save()

    def facebook_connect(self, user_data):
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
        return user'''

    def process_request(self, request):
        state = request.GET.get('state', '')
        if state == 'facebook':
            print 'cool'
            '''oauth_code = request.GET.get('code', '')
            if oauth_code != '':
                redirect_uri = get_domain(request) + '/'
                token_url = self.build_token_url(oauth_code, redirect_uri)
                access_token, _ = self.get_access_token_expire(token_url)
                # Store access token in session
                request.session['facebook_access_token'] = access_token
                user_data = self.get_current_user_data(access_token)
                if user_data is not None:
                    if request.user.is_authenticated():
                        self.unbind_facebook_account(user_data)
                        self.bind_facebook_account(request.user, user_data)
                    else:
                        user = self.facebook_connect(user_data)
                        instant_login(request, user)
                    return HttpResponsePermanentRedirect(redirect_uri + '#')'''
