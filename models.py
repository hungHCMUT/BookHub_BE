from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'User'
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Email = Column(String(255), nullable=False)
    Username = Column(String(255), nullable=False)
    Password = Column(String(255), nullable=False)
    Streak = Column(Integer, default=0)


class Membership(Base):
    __tablename__ = 'Membership'
    UserID = Column(Integer, ForeignKey('User.UserID'), primary_key=True)
    Type = Column(String(255), default="Silver")
    ExpiredDay = Column(Date)
    RemainingBooks = Column(Integer, default=1)


class TransactionMethod(Base):
    __tablename__ = 'TransactionMethod'
    Type = Column(String(255), primary_key=True)
    CardNumber = Column(String(16))


class Transaction(Base):
    __tablename__ = 'Transaction'
    TransactionID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('User.UserID'))
    Price = Column(DECIMAL(10, 2))
    TransactionDate = Column(DateTime)


class Book(Base):
    __tablename__ = 'Book'
    BookID = Column(Integer, primary_key=True,
                    autoincrement=True)  # renamed to id
    Title = Column(String(255))
    Author = Column(String(255))
    PublicationDate = Column(Date)
    Rating = Column(DECIMAL(3, 2))
    ReleaseDate = Column(Date)


class Access(Base):
    __tablename__ = 'Access'
    UserID = Column(Integer, ForeignKey('User.UserID'), primary_key=True)
    BookID = Column(Integer, ForeignKey('Book.BookID'), primary_key=True)
    AccessDate = Column(Date)


class Feedback(Base):
    __tablename__ = 'Feedback'
    UserID = Column(Integer, ForeignKey('User.UserID'), primary_key=True)
    BookID = Column(Integer, ForeignKey('Book.BookID'), primary_key=True)
    Comment = Column(Text)
    Rating = Column(DECIMAL(3, 2))
    Time = Column(DateTime)


class Leaderboard(Base):
    __tablename__ = 'Leaderboard'
    UserID = Column(Integer, ForeignKey('User.UserID'), primary_key=True)


class Friend(Base):
    __tablename__ = 'Friend'
    UserID = Column(Integer, ForeignKey('User.UserID'), primary_key=True)
    FriendUserID = Column(Integer, ForeignKey('User.UserID'), primary_key=True)
    Status = Column(String(255))
