from sqlalchemy import Column, Float, Integer, Text, text

from scryfall_clone.db.engine import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    artist = Column(Text)
    asciiName = Column(Text)
    availability = Column(Text)
    boosterTypes = Column(Text)
    borderColor = Column(Text)
    cardKingdomEtchedId = Column(Text)
    cardKingdomFoilId = Column(Text)
    cardKingdomId = Column(Text)
    cardParts = Column(Text)
    cardsphereId = Column(Text)
    colorIdentity = Column(Text)
    colorIndicator = Column(Text)
    colors = Column(Text)
    convertedManaCost = Column(Float)
    duelDeck = Column(Text)
    edhrecRank = Column(Integer)
    faceConvertedManaCost = Column(Float)
    faceFlavorName = Column(Text)
    faceManaValue = Column(Float)
    faceName = Column(Text)
    finishes = Column(Text)
    flavorName = Column(Text)
    flavorText = Column(Text)
    frameEffects = Column(Text)
    frameVersion = Column(Text)
    hand = Column(Text)
    hasAlternativeDeckLimit = Column(Integer, nullable=False, server_default=text("0"))
    hasContentWarning = Column(Integer, nullable=False, server_default=text("0"))
    hasFoil = Column(Integer, nullable=False, server_default=text("0"))
    hasNonFoil = Column(Integer, nullable=False, server_default=text("0"))
    isAlternative = Column(Integer, nullable=False, server_default=text("0"))
    isFullArt = Column(Integer, nullable=False, server_default=text("0"))
    isFunny = Column(Integer, nullable=False, server_default=text("0"))
    isOnlineOnly = Column(Integer, nullable=False, server_default=text("0"))
    isOversized = Column(Integer, nullable=False, server_default=text("0"))
    isPromo = Column(Integer, nullable=False, server_default=text("0"))
    isRebalanced = Column(Integer, nullable=False, server_default=text("0"))
    isReprint = Column(Integer, nullable=False, server_default=text("0"))
    isReserved = Column(Integer, nullable=False, server_default=text("0"))
    isStarter = Column(Integer, nullable=False, server_default=text("0"))
    isStorySpotlight = Column(Integer, nullable=False, server_default=text("0"))
    isTextless = Column(Integer, nullable=False, server_default=text("0"))
    isTimeshifted = Column(Integer, nullable=False, server_default=text("0"))
    keywords = Column(Text)
    language = Column(Text)
    layout = Column(Text)
    leadershipSkills = Column(Text)
    life = Column(Text)
    loyalty = Column(Text)
    manaCost = Column(Text)
    manaValue = Column(Float)
    mcmId = Column(Text)
    mcmMetaId = Column(Text)
    mtgArenaId = Column(Text)
    mtgjsonV4Id = Column(Text)
    mtgoFoilId = Column(Text)
    mtgoId = Column(Text)
    multiverseId = Column(Text)
    name = Column(Text)
    number = Column(Text)
    originalPrintings = Column(Text)
    originalReleaseDate = Column(Text)
    originalText = Column(Text)
    originalType = Column(Text)
    otherFaceIds = Column(Text)
    power = Column(Text)
    printings = Column(Text)
    promoTypes = Column(Text)
    purchaseUrls = Column(Text)
    rarity = Column(Text)
    rebalancedPrintings = Column(Text)
    scryfallId = Column(Text)
    scryfallIllustrationId = Column(Text)
    scryfallOracleId = Column(Text)
    securityStamp = Column(Text)
    setCode = Column(Text)
    side = Column(Text)
    signature = Column(Text)
    subtypes = Column(Text)
    supertypes = Column(Text)
    tcgplayerEtchedProductId = Column(Text)
    tcgplayerProductId = Column(Text)
    text = Column(Text)
    toughness = Column(Text)
    type = Column(Text)
    types = Column(Text)
    uuid = Column(Text(36), nullable=False)
    variations = Column(Text)
    watermark = Column(Text)
