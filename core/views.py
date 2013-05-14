from django.http import HttpResponse
from django.utils import simplejson
from firebase import firebase
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    '''fb_obj = firebase.FirebaseApplication('https://hackbase.firebaseio.com/')
    data = {'name': 'Sean Li', 'age': 22, 'email': 'lishang106@gmail.com'}
    result = fb_obj.put('/users/', 'sean', data)
    return HttpResponse('DONE')'''
    context = RequestContext(request)
    return render_to_response('index.html', context)
