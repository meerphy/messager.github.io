import sqlalchemy
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import orm


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='No info')
    site = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='No info')
    birthday = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    avatar = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='static/img/default.jpg')
    city_weather = sqlalchemy.Column(sqlalchemy.Integer, default='Murmansk,RU')
    city_id = sqlalchemy.Column(sqlalchemy.Integer, default=524304)
    news = orm.relationship("News", back_populates='user')

    def __repr__(self):
        return f'<User> {self.id} {self.name} {self.email}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)