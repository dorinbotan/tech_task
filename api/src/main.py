from .db import titles_collection
from fastapi import FastAPI, Response, status
from typing import Optional

api = FastAPI()

@api.get("/api/titles")
async def titles(title_class: Optional[str] = None, _sort: Optional[str] = None, _order: Optional[str] = None, _page: Optional[int] = None, _limit: Optional[int] = 100):
    titles = []
    async for title in titles_collection.find({}, {"_id": 0, "id": 1, "title_number": 1, "title_class": 1}).limit(_limit):
        titles.append(title)

    return titles

@api.get("/api/titles/{id}")
async def titles(id: int, response: Response):
    return None
