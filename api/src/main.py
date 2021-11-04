from fastapi import FastAPI, Response, status
from typing import Optional

api = FastAPI()

@api.get("/api/titles")
async def titles(title_class: Optional[str] = None, _sort: Optional[str] = None, _order: Optional[str] = None, _page: Optional[int] = None, _limit: Optional[int] = 100):
    return None

@api.get("/api/titles/{id}")
async def titles(id: int, response: Response):
    return None
