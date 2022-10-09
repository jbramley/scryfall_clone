import shlex

import sqlalchemy
from sqlalchemy import select
from sqlalchemy.orm import Session

from scryfall_clone import models


class InvalidQueryTerm(Exception):
    pass


def _add_column_query_term(col, query):
    match col:
        case "o" | "oracle":
            return models.Card.text.contains(query)
        case "t" | "type":
            return sqlalchemy.func.lower(models.Card.types) == query.lower()
        case _:
            raise InvalidQueryTerm(query)


def _add_query_term(query):
    match query.split(":"):
        case [q]:
            return models.Card.name.contains(q)
        case [k, q]:
            return _add_column_query_term(k, q)
        case _:
            raise InvalidQueryTerm(query)


class CardSearch:
    def __init__(self, session: Session):
        self._session = session

    async def search_on_query(self, query: str) -> list[models.Card]:
        query_terms = shlex.split(query)
        stmt = select(models.Card)
        errors = []
        wheres = []
        for q in query_terms:
            try:
                wheres.append(_add_query_term(q))
            except InvalidQueryTerm as e:
                errors.append(e.args)
        db_q = await self._session.execute(stmt.where(*wheres))
        return db_q.scalars().all()
