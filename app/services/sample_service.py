from fastapi import Depends, HTTPException

from app.repositories import SampleRepository


# todo check how to DI correctly
class SampleService:
    def __init__(self, sample_repo: SampleRepository = Depends(SampleRepository)):
        self.sample_repo = sample_repo

    async def findById(self, sample_id: int):
        res = await self.sample_repo.find(sample_id=sample_id)
        if not res:
            raise HTTPException(status_code=404, detail="Sample not found")
        return res

    def __call__(self):
        return self
