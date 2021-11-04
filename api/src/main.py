from .db import titles_collection
from fastapi import FastAPI, Path, Response, status
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
    if (id < 0):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
        
    title = await titles_collection.find_one({ "id": str(id) }, {"_id": 0})

    if title is not None:
        return title
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return
