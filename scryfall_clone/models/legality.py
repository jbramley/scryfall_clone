from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from scryfall_clone.db.engine import Base


class Legality(Base):
    __tablename__ = "legalities"

    id = Column(Integer, primary_key=True)
    format = Column(Text)
    status = Column(Text)
    uuid = Column(ForeignKey("cards.uuid"))

    card = relationship("Card")
