from django.utils.translation import gettext

from BayanTasks.utils.exception import UnAuthorizedException

__author__ = 'WadeeSami'


class Authorization(object):
    @staticmethod
    def can_manage_user(logged_in_user_id, user_id):
        if int(logged_in_user_id) != int(user_id):
            raise UnAuthorizedException()

    @staticmethod
    def can_change_password(logged_in_user_id, user_id):
        Authorization.can_manage_user(logged_in_user_id=logged_in_user_id,
                                      user_id=user_id)

