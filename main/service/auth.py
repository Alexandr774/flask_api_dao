import calendar
import datetime
from flask import abort
import jwt

from main.helpers.constans import JWT_SECRET, JWT_ALGORITHM


class AuthService:
    def __init__(self, user_s):
        self.user_service = user_s

    def generate_token(self, username, password, is_refresh=False):
        print(username)
        user = self.user_service.get_by_user_name(username)
        if user is None:
            raise abort(404)

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        min180 = datetime.datetime.utcnow() + datetime.timedelta(minutes=180)
        data["exp"] = calendar.timegm(min180.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def refresh_token(self, token):
        data = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        username = data['username']
        return self.generate_token(username, None, is_refresh=True)
