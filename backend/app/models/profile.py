# app/models/profile.py
from sqlalchemy import Column, ForeignKey, String, Date, Integer  # Integer 추가
from sqlalchemy.orm import relationship
from app.db.base import Base

class Profile(Base):
    __tablename__ = "profiles"

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    nickname = Column(String, nullable=False)
    birthday = Column(Date, nullable=True)
    avatar_url = Column(String, nullable=True)
    reading_level = Column(Integer, default=1)

    # Relationship
    user = relationship("User", back_populates="profile")