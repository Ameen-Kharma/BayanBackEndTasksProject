from BayanTasks.helper.exception_helper import BayanAPIException, ERROR

__author__ = 'WadeeSami'


class UnAuthorizedException(BayanAPIException):
    severity = ERROR
    status_code = 403
    default_detail = "You are not authorized"


class ForbiddenException(BayanAPIException):
    severity = ERROR
    status_code = 401
    default_detail = "Authentication Failed"


class ResourceException(BayanAPIException):
    severity = ERROR
    # status_code = StatusCodes.ERROR


class InvalidCredentialsException(BayanAPIException):
    severity = ERROR
    status_code = 601
    default_detail = "Invalid Credentials"


class UserAlreadyExistsException(BayanAPIException):
    severity = ERROR
   # status_code = StatusCodes.USER_ALREADY_EXISTS


class UserNotVerifiedException(BayanAPIException):
    severity = ERROR
   # status_code = StatusCodes.USER_NOT_VERIFIED


class UserNotAllowedToReSendCodeException(BayanAPIException):
    severity = ERROR
    #status_code = StatusCodes.USER_EXCEED_NUMBER_OF_ALLOWED_VERIFICATION_CODE


class InvalidVerificationCodeException(BayanAPIException):
    severity = ERROR
   # status_code = StatusCodes.INVALID_VERIFICATION_CODE


class PhoneNumberAlreadyVerifiedException(BayanAPIException):
    severity = ERROR
    #status_code = StatusCodes.USER_PHONE_ALREADY_VERIFIED


class ExceedNumberOfAllowedVerifyPhoneNumberException(ForbiddenException):
    severity = ERROR
    status_code = 608


class ExceedNumberOfAllowedResetPasswordException(BayanAPIException):
    severity = ERROR
   # status_code = StatusCodes.EXCEED_NUMBER_OF_ALLOWED_RESET_PASSWORD


class UserEmailNotVerifiedException(BayanAPIException):
    severity = ERROR
    #status_code = StatusCodes.USER_EMAIL_NOT_VERIFIED


class SQSError(BayanAPIException):
    pass


class InvalidUserResetPasswordCodeException(BayanAPIException):
    severity = ERROR
   # status_code = StatusCodes.INVALID_USER_RESET_PASSWORD_CODE