from .db import titles_collection
from fastapi import FastAPI, Path, Response, status
from typing import Optional

api = FastAPI()

@api.get("/api/titles")
async def titles(title_class: Optional[str] = None, _sort: Optional[str] = None, _order: Optional[str] = None, _page: Optional[int] = 0, _limit: Optional[int] = 100):
    # TODO: ignore case
    # Filter values by title_class
    if title_class is not None:
        filter = { "title_class": title_class }
    else:
        filter = {}

    # Sort values by given key in the given order (by default order ascending by id)
    sort = []
    if _sort is not None:
        _sort = _sort.split(',')
        _order = _order.split(',')

        for combination in zip(_sort, _order):
            sort.append([combination[0], -1 if (combination[1] == 'desc') else 1])
    else:
        sort = [( "id", 1 )]

    skip = _page * _limit

    titles = []
    async for title in titles_collection.find(filter, {"_id": 0, "content": 0}).sort(sort).skip(skip).limit(_limit):
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
