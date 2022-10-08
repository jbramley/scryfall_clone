import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SetInDBBase(BaseModel):
    id: int
    base_set_size: int = Field(alias="baseSetSize")
    block: Optional[str]
    booster: Optional[str]
    code: str
    release_date: Optional[datetime.date] = Field(alias="releaseDate")
    type: str

    class Config:
        orm_mode = True


class Set(SetInDBBase):
    pass
