from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from scryfall_clone import schemas
from scryfall_clone.api.deps import get_db
from scryfall_clone.core.card_search import CardSearch

router = APIRouter()


@router.get("/search", response_model=list[schemas.Card])
async def card_search(q: str, db: Session = Depends(get_db)) -> list[schemas.Card]:
    search = CardSearch(db)
    return await search.search_on_query(q)
