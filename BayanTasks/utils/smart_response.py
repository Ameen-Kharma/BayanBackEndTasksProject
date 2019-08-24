from gettext import gettext

from rest_framework.response import Response

from BayanTasks.constant import StatusCodes


class Messages(object):
    RESPONSE = {
        100: {'message': gettext('CONTINUE')},
        101: {'message': gettext('SWITCHING_PROTOCOLS')},
        StatusCodes.OK: {'message': gettext('SUCCESS')},
        201: {'message': gettext('CREATED')},
        202: {'message': gettext('ACCEPTED')},
        203: {'message': gettext('NON_AUTHORITATIVE_INFORMATION')},
        204: {'message': gettext('NO_CONTENT')},
        205: {'message': gettext('RESET_CONTENT')},
        206: {'message': gettext('PARTIAL_CONTENT')},
        300: {'message': gettext('MULTIPLE_CHOICES')},
        301: {'message': gettext('MOVED_PERMANENTLY')},
        302: {'message': gettext('FOUND')},
        303: {'message': gettext('SEE_OTHER')},
        304: {'message': gettext('BAD_REQUEST')},
        305: {'message': gettext('USE_PROXY')},
        306: {'message': gettext('RESERVED')},
        307: {'message': gettext('TEMPORARY_REDIRECT')},
        400: {'message': gettext('BAD_REQUEST')},
        401: {'message': gettext('UNAUTHORIZED')},
        402: {'message': gettext('PAYMENT_REQUIRED')},
        403: {'message': gettext('FORBIDDEN')},
        404: {'message': gettext('NOT_FOUND')},
        405: {'message': gettext('METHOD_NOT_ALLOWED')},
        406: {'message': gettext('NOT_ACCEPTABLE')},
        407: {'message': gettext('PROXY_AUTHENTICATION_REQUIRED')},
        408: {'message': gettext('REQUEST_TIMEOUT')},
        409: {'message': gettext('CONFLICT')},
        410: {'message': gettext('GONE')},
        411: {'message': gettext('LENGTH_REQUIRED')},
        412: {'message': gettext('PRECONDITION_FAILED')},
        413: {'message': gettext('REQUEST_ENTITY_TOO_LARGE')},
        414: {'message': gettext('REQUEST_URI_TOO_LONG')},
        415: {'message': gettext('UNSUPPORTED_MEDIA_TYPE')},
        416: {'message': gettext('REQUESTED_RANGE_NOT_SATISFIABLE')},
        # 417: {'message': gettext('PIN_AUTHENTICATION_FAILED')},
        417: {'message': gettext('EXPECTATION_FAILED')},
        428: {'message': gettext('PRECONDITION_REQUIRED')},
        429: {'message': gettext('TOO_MANY_REQUESTS')},
        431: {'message': gettext('REQUEST_HEADER_FIELDS_TOO_LARGE')},
        451: {'message': gettext('UNAVAILABLE_FOR_LEGAL_REASONS')},
        500: {'message': gettext('INTERNAL_SERVER_ERROR')},
        501: {'message': gettext('NOT_IMPLEMENTED')},
        502: {'message': gettext('BAD_GATEWAY')},
        503: {'message': gettext('SERVICE_UNAVAILABLE')},
        504: {'message': gettext('GATEWAY_TIMEOUT')},
        505: {'message': gettext('HTTP_VERSION_NOT_SUPPORTED')},
        511: {'message': gettext('NETWORK_AUTHENTICATION_REQUIRED')},
        1312: {'message': gettext('INVALID_JSON')}
    }

    SPECIAL_RESPONSE = {
         StatusCodes.ERROR: {'message': gettext('ERROR')},
         StatusCodes.INVALID_CREDENTIALS: {'message': gettext('INVALID_CREDENTIALS')},
         StatusCodes.USER_ALREADY_EXISTS: {'message': gettext('USER_ALREADY_EXISTS')},
        # StatusCodes.USER_NOT_VERIFIED: {'message': gettext('USER_NOT_VERIFIED')},
        # StatusCodes.USER_EXCEED_NUMBER_OF_ALLOWED_VERIFICATION_CODE: {'message': gettext('USER_EXCEED_NUMBER_OF_ALLOWED_VERIFICATION_CODE')},
        # StatusCodes.EXCEED_NUMBER_OF_ALLOWED_RESET_PASSWORD:{'message':gettext('EXCEED_NUMBER_OF_ALLOWED_RESET_PASSWORD')},
        # StatusCodes.User_Exceeds_Allowed_Times_To_Verify_Phone_Number: {'message': gettext('USER_EXCEEDS_ALLOWED_TIMES_TO_VERIFY_PHONE_NUMBER')},
        # 609: {'message': gettext('USER_ALREADY_DONE_ACTION')},
        # StatusCodes.USER_EMAIL_NOT_VERIFIED: {'message': gettext('USER_EMAIL_NOT_VERIFIED')},
        # StatusCodes.USER_PHONE_ALREADY_VERIFIED: {'message': gettext('USER_PHONE_ALREADY_VERIFIED')},
        # StatusCodes.INVALID_VERIFICATION_CODE: {'message': gettext('Invalid Verification Code')},
        # StatusCodes.INVALID_USER_RESET_PASSWORD_CODE: {'message': gettext('INVALID_RESET_PASSWORD_CODE')},
    }


def smart_response(data, status_code, message_code=None, template_name=None, headers=None, exception=False, content_type=None):
    if message_code:
        status_message = message_code
    elif status_code in Messages.RESPONSE:
        status_message = Messages.RESPONSE[status_code]['message']
    elif status_code in Messages.SPECIAL_RESPONSE:
        status_message = Messages.SPECIAL_RESPONSE[status_code]['message']
    else:
        status_message = ""

    if type(data) is str:
        data = {"message": data}

    response = {'data': data, 'status': status_message, 'status_code': status_code}

    external_status_code = 200
    if status_code == 500:
        external_status_code = 500

    return Response(response, external_status_code, template_name, headers, exception, content_type)
