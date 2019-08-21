from django.utils.crypto import get_random_string
from BayanTasks.constant import PASSWORD_SALT_LENGTH
from BayanTasks.utils.helpers import encrypt_password
from BayanTasks.repositories.use_repositories import UserRepo

class UserComponent:
    """
    this class doing the logic for the user controller such as registration ans login and other logic

    """
    def __init__(self):
        pass


    @staticmethod
    def create_user(user_name, user_email, plain_password):
        if user_name is None or user_email is None or plain_password is None:
            raise Exception

        user = UserRepo.get_user_by_email(email=user_email)
        if user is not None:
            raise Exception

        user_salt = UserComponent.generate_user_random_salt()
        encrypted_passwrd = encrypt_password(plain_password=plain_password, salt=user_salt)
        user = UserRepo.create_user(user_name=user_name, user_email=user_email,
                                    encrypted_password=encrypted_passwrd, user_salt=user_salt, commit=True)
        return user

    @staticmethod
    def login(request, user_email, plain_password):
        user = UserRepo.get_user_by_email(email=user_email)
        if user is not None:
            user_password_salt = user.user_salt
            user_database_password = user.encrypted_password
            encrypted_password = encrypt_password(plain_password, user_password_salt)

            if user_database_password == encrypted_password:
                request.session['user_id'] = user.id
                request.session['user_type'] = user.type
                return user
            else:
                raise Exception

        else:
            raise Exception

    @staticmethod
    def logout(request):
        request.session.flush()

    @staticmethod
    def generate_user_random_salt():
        salt = get_random_string(length=PASSWORD_SALT_LENGTH)
        return salt
