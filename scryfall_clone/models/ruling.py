from sqlalchemy import Column, Date, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from scryfall_clone.db.engine import Base


class Ruling(Base):
    __tablename__ = "rulings"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    text = Column(Text)
    uuid = Column(ForeignKey("cards.uuid"))

    card = relationship("Card")
