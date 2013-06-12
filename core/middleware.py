from core.utils.network import get_domain
from core.utils.auth import instant_login
from django.http import HttpResponsePermanentRedirect
from core.utils.facebook import (get_access_token_expire,
    get_facebook_user_data, unbind_facebook_account, bind_facebook_account,
    facebook_connect)


class FacebookMiddleware(object):

    def process_request(self, request):
        if 'next' in request.GET:
            request.session['login_redirect_url'] = request.GET['next']
        state = request.GET.get('state', '')
        # Check if request is from Facebook
        if state == 'facebook':
            oauth_code = request.GET.get('code', '')
            if oauth_code != '':
                redirect_uri = get_domain(request) + '/'
                access_token, expires = get_access_token_expire(oauth_code, redirect_uri)
                # Store access token in session
                request.session['facebook_access_token'] = access_token
                request.session['facebook_expires'] = expires
                user_data = get_facebook_user_data(access_token)
                if user_data is not None:
                    if request.user.is_authenticated():
                        unbind_facebook_account(user_data)
                        bind_facebook_account(request.user, user_data)
                    else:
                        user = facebook_connect(user_data)
                        instant_login(request, user)
                    if 'login_redirect_url' in request.session:
                        login_redirect_url = request.session['login_redirect_url'] + '#/'
                    else:
                        login_redirect_url = '/#/'
                    return HttpResponsePermanentRedirect(login_redirect_url)
