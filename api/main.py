from fastapi import FastAPI
from pydantic import BaseModel

from services.search_service import SearchService


app = FastAPI()

search_service = SearchService()


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query(request: QueryRequest):

    result = search_service.search(request.query)

    return result


@app.get("/cache/stats")
def cache_stats():

    return search_service.cache.stats()


@app.delete("/cache")
def clear_cache():

    search_service.cache.clear()

    return {"message": "Cache cleared"}