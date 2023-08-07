from main.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_by_name(self, name):
        data = self.session.query(User).filter(User.username == name).first()
        return data

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return 'ok'

    def update(self, user):
        self.session.add(user)
        self.session.commit()

    def get_all(self):
        get_all = self.session.query(User).all()
        return get_all
