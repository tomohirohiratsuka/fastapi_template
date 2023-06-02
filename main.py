from typing import Optional

from fastapi import FastAPI

from app.routers import sample_router

app = FastAPI()
app.include_router(sample_router.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
