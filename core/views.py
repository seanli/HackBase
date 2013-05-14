from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
import urllib
from core.utilities import get_domain
from django.conf import settings
from django.contrib import auth


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def facebook_login(request):
    login_link = 'https://www.facebook.com/dialog/oauth?' + urllib.urlencode(
        {
            'client_id': settings.FACEBOOK_APP_ID,
            'redirect_uri': get_domain(request) + '/',
            'response_type': 'code',
            'scope': 'email',
            'state': 'facebook',
        }
    )
    return HttpResponseRedirect(login_link)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
