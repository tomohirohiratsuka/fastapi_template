from pydantic import BaseModel


class SampleBase(BaseModel):
    name: str
    age: int


class SampleCreate(SampleBase):
    email: str
