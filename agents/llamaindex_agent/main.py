from fastapi import FastAPI
from pydantic import BaseModel
from query_engine import query_index

app = FastAPI(title="LlamaIndex Agent")

class SearchRequest(BaseModel):
    query: str

class SearchResponse(BaseModel):
    context: str

@app.post("/search", response_model=SearchResponse)
async def search_book(request: SearchRequest):
    context = query_index(request.query)
    return SearchResponse(context=context)
