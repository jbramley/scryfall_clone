from scryfall_clone.db.engine import SessionLocal


async def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        await db.close()
