from typing import Optional

from pydantic import BaseModel, Field


class CardInDBBase(BaseModel):
    id: int
    name: str
    manaCost: Optional[str]
    rarity: str
    set_code: str = Field(alias="setCode")
    types: str
    keywords: Optional[str]
    text: str

    class Config:
        orm_mode = True


class Card(CardInDBBase):
    pass
