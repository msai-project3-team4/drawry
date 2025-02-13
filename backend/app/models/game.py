from sqlalchemy import Column, ForeignKey, Integer, Float, String, DateTime, Enum
import enum
from sqlalchemy.orm import relationship
from app.db.base import Base

class GameType(enum.Enum):
    word_search = "word_search"
    memory_match = "memory_match"
    spelling_bee = "spelling_bee"
    sentence_arrange = "sentence_arrange"
    story_puzzle = "story_puzzle"

class Game(Base):
    __tablename__ = "games"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    game_type = Column(Enum(GameType), nullable=False)
    score = Column(Float, default=0)
    completion_time = Column(Float, nullable=True)  # in seconds
    difficulty_level = Column(Integer, default=1)
    completed_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="games")
    book = relationship("Book", back_populates="games")