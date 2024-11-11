from sqlalchemy.orm import Session
from schemas import users, books, membership, friends
from models import User, Book, Membership, Friend


# User
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.UserID == user_id).first()


def get_user_list(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: users.UserCreate):
    db_user = User(Email=user.Email,
                   Username=user.Username,
                   Password=user.Password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    silver_membership = Membership(
        UserID=db_user.UserID,
        Type="Silver",
        RemainingBooks=1  # Example default for a silver membership
    )
    db.add(silver_membership)
    db.commit()
    db.refresh(silver_membership)
    return db_user


def update_user(db: Session, user_id: int, user_update: users.UserUpdate):
    user = db.query(User).filter(User.UserID == user_id).first()
    if not user:
        return None

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.UserID == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user


# Book
def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.BookID == book_id).first()


def get_book_list(db: Session):
    return db.query(Book).all()


def create_book(db: Session, book: books.BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: int, book_update: books.BookUpdate):
    book = db.query(Book).filter(Book.BookID == book_id).first()
    if not book:
        return None

    for key, value in book_update.dict(exclude_unset=True).items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.BookID == book_id).first()
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book


# Membership
def get_membership_by_id(db: Session, user_id: int):
    return db.query(Membership).filter(Membership.UserID == user_id).first()


def get_membership_list(db: Session):
    return db.query(Membership).all()


def create_membership(db: Session, membership_create: membership.MembershipCreate, user_id: int):
    db_membership = Membership(UserID=user_id,
                               Type=membership_create.Type,
                               ExpiredDay=membership_create.ExpiredDay,
                               RemainingBooks=membership_create.RemainingBooks)
    db.add(db_membership)
    db.commit()
    db.refresh(db_membership)
    return db_membership


def update_membership(db: Session, user_id: int, membership_update: membership.MembershipUpdate):
    new_membership = db.query(Membership).filter(
        Membership.UserID == user_id).first()
    if not new_membership:
        return None

    for key, value in membership_update.dict(exclude_unset=True).items():
        setattr(new_membership, key, value)

    db.commit()
    db.refresh(new_membership)
    return new_membership


def delete_membership(db: Session, user_id: int):
    membership_retrieve = db.query(Membership).filter(
        Membership.UserID == user_id).first()
    if not membership_retrieve:
        return None
    db.delete(membership_retrieve)
    db.commit()
    return membership_retrieve


# Friend
def create_friend(db: Session, friend: friends.UserFriendshipCreate, user_id: int):
    db_friend = Friend(UserID=user_id,
                       FriendUserID=friend.FriendUserId,
                       Status=friend.Status)
    db.add(db_friend)
    db.commit()
    db.refresh(db_friend)
    return db_friend


def get_friend_by_id(db: Session, user_id: int):
    return db.query(Friend).filter(Friend.UserID == user_id).first()


def get_friend_list(db: Session):
    return db.query(Friend).all()


def update_friend(db: Session, user_id: int, friend_update: friends.UserFriendshipUpdate):
    new_friend = db.query(Friend).filter(
        Friend.UserID == user_id).first()
    if not new_friend:
        return None

    for key, value in friend_update.dict(exclude_unset=True).items():
        setattr(new_friend, key, value)

    db.commit()
    db.refresh(new_friend)
    return new_friend


def delete_friend(db: Session, user_id: int):
    friend_retrieve = db.query(Friend).filter(
        Friend.UserID == user_id).first()
    if not friend_retrieve:
        return None
    db.delete(friend_retrieve)
    db.commit()
    return friend_retrieve
