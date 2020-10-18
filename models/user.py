import sqlite3
from db import db

class UserModel(db.Model):
     __tablename__ = 'users'
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(80))
     password = db.Column(db.String(80))
     
     def __init__(self, username, password):
        self.username = username
        self.password = password

     @classmethod
     def find_by_name(cls, username):
         return cls.query.filter_by(username=username).first()

     @classmethod
     def find_by_id(cls, _id):
         return cls.query.filter_by(id=_id).first()

     def save_to_db(self):
         db.session.add(self)
         db.session.commit()
    # @classmethod
    # def find_by_username(cls, username):
    #     conn = sqlite3.connect('data.db')
    #     curs = conn.cursor()
    #     select_query = ('SELECT * from users WHERE username = ?')
    #     res = curs.execute(select_query, (username,))
    #     row = res.fetchone()
    #     if row:
    #         user =  cls(*row)
    #     else:
    #         user = None

    #     conn.close()
    #     return user

    # @classmethod
    # def find_by_id(cls, _id):
    #     conn = sqlite3.connect('data.db')
    #     curs = conn.cursor()
    #     select_query = ('SELECT * from users WHERE id = ?')
    #     res = curs.execute(select_query, (_id,))
    #     row = res.fetchone()
    #     if row:
    #         user =  cls(*row)
    #     else:
    #         user = None

    #     conn.close()
    #     return user