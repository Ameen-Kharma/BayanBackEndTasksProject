from BayanTasks.models.user import User, UserAddress, Task
from common.libs.bayan_db import db_session
from BayanTasks.constant import UserType
from sqlalchemy.orm import load_only
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

    @staticmethod
    def get_user_address():
        query = db_session.query(UserAddress)
        result = query.one_or_none()
        return result

    @staticmethod
    def get_user_tasks_by_user_id(user_id):

        query = db_session.query(Task).filter(Task.user_id == user_id)
        result = query.all()

        return result
