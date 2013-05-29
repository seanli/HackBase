from django.conf import settings as django_settings


def settings(request):
    '''
    Adds the settings specified in settings.TEMPLATE_VISIBLE_SETTINGS to the request context.
    '''
    context = {}
    for attr in django_settings.TEMPLATE_VISIBLE_SETTINGS:
        try:
            context[attr] = getattr(django_settings, attr)
        except AttributeError:
            context[attr] = None
    return context
