from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

subscription =Table('subscription',Base.metadata,
  Column('id_user', Integer, ForeignKey('users.id')),
  Column('id_subscriber', Integer, ForeignKey('users.id'))
)
# class Subscription(Base):
#     __tablename__ = 'subscription'
#     id = Column(Integer, primary_key=True)
#     id_user = Column(Integer, ForeignKey('users.id'))
#     id_subscriber = Column(Integer, ForeignKey('users.id'))
#
#     def __repr__(self):
#         return "<Subscription(id={}, id_user={}, id_subscriber={} )>" \
#             .format(self.id, self.id_user, self.subscriber)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(Text)
    password = Column(Text)
    name = Column(Text)
    status = Column(Text)
    admin = Column(Text)
    comments=relationship("Comment", cascade="all, delete", backref="users")
    posts = relationship("Post",cascade="all, delete", backref="users")
    id_sub = relationship('User',
        secondary=subscription,
        primaryjoin=(subscription.c.id_user == id),
        secondaryjoin=(subscription.c.id_subscriber == id),
        backref=backref('subscriber', lazy='dynamic'),
        lazy='dynamic')

    def __repr__(self):
        return "<User(id={}, login='{}', password='{}', name='{}', status='{}', admin='{}' )>" \
            .format(self.id, self.login, self.password, self.name, self.status, self.admin)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    theme = Column(Text)
    text = Column(Text)
    rating = Column(Integer)
    id_user = Column(Integer, ForeignKey('users.id'))
    comments = relationship("Comment", cascade="all, delete", backref="posts")
    def __repr__(self):
        return "<Post(id={}, name='{}', theme='{}', text='{}', rating={}, id_user={} )>" \
            .format(self.id, self.name, self.theme, self.text, self.rating, self.id_user)


parent_comments=Table('parent_comments', Base.metadata,
  Column('id_parent', Integer, ForeignKey('comments.id')),
  Column('id_child', Integer, ForeignKey('comments.id'))
)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    rating = Column(Integer)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_post = Column(Integer, ForeignKey('posts.id'))
    parent = relationship('Comment',cascade="all, delete",
     secondary=parent_comments,
     primaryjoin=(parent_comments.c.id_parent == id),
    secondaryjoin = (parent_comments.c.id_child == id),
                    backref = backref('child', lazy='dynamic',),
                              lazy = 'dynamic')
    def __repr__(self):
        return "<Comment(id={}, text='{}', rating={}, id_user={}, id_post={} )>" \
            .format(self.id, self.text, self.rating, self.id_user,self.id_post)
