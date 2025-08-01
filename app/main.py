from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import QueryRequest
from app.agent import agent

app = FastAPI()

# Enable CORS for frontend use
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
async def query_endpoint(request: QueryRequest):
    try:
        response = agent.run(request.question)
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}
