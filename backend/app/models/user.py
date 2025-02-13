from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    last_login_at = Column(DateTime, nullable=True)

    # Relationships
    profile = relationship("Profile", back_populates="user", uselist=False)
    books = relationship("Book", back_populates="user")
    games = relationship("Game", back_populates="user")
    tracking_data = relationship("Tracking", back_populates="user")