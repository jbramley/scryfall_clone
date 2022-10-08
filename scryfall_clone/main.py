from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session

from scryfall_clone import models, schemas
from scryfall_clone.db.engine import SessionLocal

app = FastAPI()


async def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        await db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sets/")
async def card_set(db: Session = Depends(get_db)) -> list[schemas.Set]:
    q = await db.execute(select(models.Set))
    return q.scalars().all()


@app.get("/sets/{set_id}")
async def single_set(set_id: int, db: Session = Depends(get_db)) -> schemas.Set:
    q = await db.execute(select(models.Set).where(models.Set.id == set_id))
    return q.scalars().one()


@app.get("/keywords/")
async def keyword_list(db: Session = Depends(get_db)) -> list[str]:
    stmt = (
        select(models.Card.keywords)
        .distinct(models.Card.keywords)
        .where(models.Card.keywords is not None)
    )
    q = await db.execute(stmt)
    keyword_lists = q.scalars().all()
    keywords = set()
    for k in keyword_lists:
        keywords.update(k.split(","))
    return sorted(list(keywords))


@app.get("/keywords/{keyword}/cards", response_model=list[schemas.Card])
async def keyword_cards(
    keyword: str, db: Session = Depends(get_db)
) -> list[schemas.Card]:
    stmt = select(models.Card).where(models.Card.keywords.contains(keyword))
    q = await db.execute(stmt)
    return q.scalars().all()
