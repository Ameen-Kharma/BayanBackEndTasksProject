import traceback

from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import APIException, ErrorDetail
from rest_framework.views import set_rollback


from BayanTasks.utils.smart_response import smart_response

CRITICAL = 50
ERROR = 40
NOTSET = 0


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.
    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.
    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    headers = None
    if isinstance(exc, APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        data = exc.detail
        if type(data) is ErrorDetail:
            data = str(data)
        status_code = exc.status_code
        set_rollback()

    elif isinstance(exc, Http404):
        data = "Not Found"
        status_code = status.HTTP_404_NOT_FOUND
        set_rollback()

    else:
        data = str(exc)
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return smart_response(data, status_code=status_code, headers=headers)


# Any new custom exceptions should extend this on app level
class BayanAPIException(APIException):
    severity = CRITICAL


def bayan_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if (isinstance(exc, BayanAPIException) and exc.severity == CRITICAL) or response.status_code == 500:
        pass
        # Log all errors
        # logger = FoodsieLogger().get_logger()
        # logger.error(str(exc) + "\n" + str(traceback.format_exc()))
        # SlackService.general_error_notify(context['request'], exc)

    return response
