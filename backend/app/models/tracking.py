from sqlalchemy import Column, ForeignKey, Integer, Float, JSON, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class Tracking(Base):
    __tablename__ = "tracking"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    page_id = Column(Integer, ForeignKey("pages.id"), nullable=False)
    gaze_data = Column(JSON, nullable=True)
    reading_duration = Column(Float, default=0)  # in seconds
    focus_score = Column(Float, default=0)  # 0-100
    reading_completion = Column(Float, default=0)  # percentage
    tracked_at = Column(DateTime, nullable=False)

    # Relationships
    user = relationship("User", back_populates="tracking_data")
    book = relationship("Book", back_populates="tracking_data")
    page = relationship("Page", back_populates="tracking_data")