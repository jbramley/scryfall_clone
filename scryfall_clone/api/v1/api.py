from fastapi import APIRouter

from scryfall_clone.api.v1.endpoints import cards

api_router = APIRouter()
api_router.include_router(cards.router, prefix="/cards", tags=["cards"])
