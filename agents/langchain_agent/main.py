from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chains import run_chain

app = FastAPI(title="LangChain Agent")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

@app.post("/query", response_model=QueryResponse)
async def query_langchain_agent(request: QueryRequest):
    try:
        result = run_chain(request.query)
        return QueryResponse(response=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
