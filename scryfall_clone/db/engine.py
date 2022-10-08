import logging

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

Base = declarative_base()

engine = create_async_engine("sqlite+aiosqlite:///AllPrintings.sqlite")
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
