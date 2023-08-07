import base64
import hmac
from flask_restx import abort
from main.helpers.constans import PWD_SALT, PWD_ITERATIONS
import hashlib


class UserService:
    def __init__(self, dao):
        self.dao = dao

    def generate_password(self, password):
        """ хешированеие паролей"""
        hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_SALT,
            PWD_ITERATIONS
        )
        return base64.b64encode(hash)

    def get_by_user_name(self, name):
        return self.dao.get_by_name(name)

    def compare_password(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_SALT,
            PWD_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)

    def create(self, data) -> dict:
        data['username'] = data['email']
        data['password'] = self.generate_password(data['password'])
        del data['email']
        return self.dao.create(data)

    def update_password(self, data):
        old_password = data['old_password']
        new_password = data['new_password']
        user = self.get_by_user_name(data['username'])
        if self.compare_password(user.password, old_password) is True:
            user.password = self.generate_password(new_password)
            self.dao.update(user)

    def update_user(self, user_up):
        user = self.get_by_user_name(user_up['username'])
        user.name = user_up['name']
        user.surname = user_up['surname']
        user.favorite_genre = user_up['favourite_genre']
        self.dao.update(user)

    def get_all(self):
        return self.dao.get_all()
