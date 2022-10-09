import shlex

import sqlalchemy
from sqlalchemy import select
from sqlalchemy.orm import Session

from scryfall_clone import models


def _add_column_query_term(stmt, col, query):
    match col:
        case "o" | "oracle":
            return stmt.where(models.Card.text.contains(query))
        case "t" | "type":
            return stmt.where(sqlalchemy.func.lower(models.Card.types) == query.lower())
        case _:
            return stmt


def _add_query_term(stmt, query):
    match query.split(":"):
        case [q]:
            return stmt.where(models.Card.name.contains(q))
        case [k, q]:
            return _add_column_query_term(stmt, k, q)
        case _:
            return stmt


class CardSearch:
    def __init__(self, session: Session):
        self._session = session

    async def search_on_query(self, query: str) -> list[models.Card]:
        query_terms = shlex.split(query)
        stmt = select(models.Card)
        for q in query_terms:
            stmt = _add_query_term(stmt, q)
        db_q = await self._session.execute(stmt)
        return db_q.scalars().all()
