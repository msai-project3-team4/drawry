from sqlalchemy import Column, ForeignKey, String, Integer, Enum, DateTime
from sqlalchemy.orm import relationship
import enum
from app.db.base import Base

class BookStatus(enum.Enum):
    draft = "draft"
    completed = "completed"

class Book(Base):
    __tablename__ = "books"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    status = Column(Enum(BookStatus), default=BookStatus.draft)
    current_page_number = Column(Integer, default=1)
    total_pages = Column(Integer, default=0)
    last_edited_at = Column(DateTime, nullable=True)
    template_type = Column(String, default="aladdin")
    protagonist_type = Column(String, nullable=True)

    # Relationships
    user = relationship("User", back_populates="books")
    pages = relationship("Page", back_populates="book", cascade="all, delete-orphan")
    tracking_data = relationship("Tracking", back_populates="book")
    games = relationship("Game", back_populates="book")