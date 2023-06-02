from dotenv import dotenv_values
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ASYNC_DB_URL = "mysql+aiomysql://%s:%s@%s/%s?charset=utf8" % (
    dotenv_values(".env")["MYSQL_USER"],
    dotenv_values(".env")["MYSQL_PASSWORD"],
    dotenv_values(".env")["MYSQL_HOST"],
    dotenv_values(".env")["MYSQL_DATABASE"],
)

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)

async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)
Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session
