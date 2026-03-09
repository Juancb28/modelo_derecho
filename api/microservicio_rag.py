from fastapi import FastAPI
# from models_llm.RAG import qa_chain
from routes.api_query import router as query_router

app = FastAPI()

app.include_router(query_router)


