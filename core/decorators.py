import time
from core.utils.network import build_response
from core.utils.network import get_client_ip


# Attaches important meta data for an AJAX request
def ajax_endpoint(view_func):

    def wrapped(request, *args, **kwargs):
        benchmark_start = time.time()
        response, status = view_func(request)
        benchmark_end = time.time()
        meta_data = {}
        meta_data['request_uri'] = request.build_absolute_uri()
        meta_data['get'] = request.GET
        meta_data['post'] = request.POST
        meta_data['ip'] = get_client_ip(request)
        if 'sessionid' in request.COOKIES:
            meta_data['session_id'] = request.COOKIES['sessionid']
        if 'csrftoken' in request.COOKIES:
            meta_data['csrf_token'] = request.COOKIES['csrftoken']
        if 'HTTP_USER_AGENT' in request.META:
            meta_data['user_agent'] = request.META['HTTP_USER_AGENT']
        if request.user.is_authenticated():
            meta_data['current_user_id'] = request.user.id
        meta_data['status'] = status
        meta_data['execution_time'] = benchmark_end - benchmark_start
        response['meta'] = meta_data
        return build_response(response, status=status)

    return wrapped
