from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Sample
from database import get_db


class SampleRepository:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db

    async def find(self, sample_id: int):
        query = select(Sample).where(Sample.id == sample_id)
        result = await self.db.execute(query)
        item = result.scalars().first()
        return item
