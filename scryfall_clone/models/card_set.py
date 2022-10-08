from sqlalchemy import Column, Date, Integer, Text, text

from scryfall_clone.db.engine import Base


class Set(Base):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True)
    baseSetSize = Column(Integer)
    block = Column(Text)
    booster = Column(Text)
    cardsphereSetId = Column(Integer)
    code = Column(Text(8), nullable=False)
    isFoilOnly = Column(Integer, nullable=False, server_default=text("0"))
    isForeignOnly = Column(Integer, nullable=False, server_default=text("0"))
    isNonFoilOnly = Column(Integer, nullable=False, server_default=text("0"))
    isOnlineOnly = Column(Integer, nullable=False, server_default=text("0"))
    isPartialPreview = Column(Integer, nullable=False, server_default=text("0"))
    keyruneCode = Column(Text)
    mcmId = Column(Integer)
    mcmIdExtras = Column(Integer)
    mcmName = Column(Text)
    mtgoCode = Column(Text)
    name = Column(Text)
    parentCode = Column(Text)
    releaseDate = Column(Date)
    sealedProduct = Column(Text)
    tcgplayerGroupId = Column(Integer)
    totalSetSize = Column(Integer)
    type = Column(Text)
