from BayanTasks.models.user import User
from common.libs.bayan_db import db_session
from BayanTasks.constant import UserType
class UserRepo:

    def __init__(self):
        pass


    @staticmethod
    def create_user(user_name, user_email, user_type=UserType.CUSTOMER, encrypted_password=None, user_salt=None,
                    commit=True):
        user = User(name=user_name, email=user_email, type=user_type, encrypted_password=encrypted_password,
                    user_salt=user_salt)
        db_session.add(user)
        try:
            if commit:
                db_session.commit()
            else:
                db_session.flush()
        except Exception as e:
            print(str(e))

        return user

    @staticmethod
    def get_user_by_email(email):
        query = db_session.query(User).filter(User.email == email)
        result = query.one_or_none()
        return result


