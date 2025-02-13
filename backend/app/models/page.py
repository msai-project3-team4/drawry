from sqlalchemy import Column, ForeignKey, String, Integer, JSON, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class Page(Base):
    __tablename__ = "pages"

    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    page_number = Column(Integer, nullable=False)
    
    # Sketch related
    sketch_url = Column(String, nullable=True)
    generated_image_url = Column(String, nullable=True)
    prompt_text = Column(String, nullable=True)
    
    # Story related
    story_text = Column(String, nullable=True)
    audio_url = Column(String, nullable=True)
    
    # Editor state
    editor_state = Column(JSON, nullable=True)
    canvas_data = Column(JSON, nullable=True)
    last_edited_position = Column(JSON, nullable=True)
    is_sketch_completed = Column(Boolean, default=False)
    is_story_completed = Column(Boolean, default=False)

    # Relationships
    book = relationship("Book", back_populates="pages")
    tracking_data = relationship("Tracking", back_populates="page")