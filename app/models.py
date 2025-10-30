from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so 
from app import db

class User(db.Model):
    id : so.Mapped[int] = so.mapped_column(primary_key=True) # Primary key sütunu
    username : so.Mapped[str] = so.mapped_column(sa.String(80),index=True, unique=True) # Kullanıcı adı sütunu
    email : so.Mapped[Optional[str]] = so.mapped_column(sa.String(120), index=True, unique=True) # E-posta sütunu
    password_hash : so.Mapped[Optional[str]] = so.mapped_column(sa.String(128)) # Şifre hash sütunu

    posts: so.Mapped[Optional[list["Post"]]] = so.relationship(back_populates="author")
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id : so.Mapped[int] = so.mapped_column(primary_key=True) # Primary
    body : so.Mapped[str] = so.mapped_column(sa.String(140)) # Gönderi içeriği sütunu
    timestamp : so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc)) # Zaman damgası sütunu
    user_id : so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('user.id')) # Yabancı anahtar sütunu
    author : so.Mapped[User] = so.relationship("User", back_populates="posts") # İlişki tanımı

    def __repr__(self):
        return '<Post {}>'.format(self.body)