# from fastapi import FastAPI, HTTPException
# from config.settings import qdrant_client
# from services.checkcollection import check_and_add_collection
# from resources.rag import generate_answer
# from routers import endpoint
# from fastapi import  Request
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()

# # app.mount("/static", StaticFiles(directory="frontend"), name="static")
# # Include the router
# app.include_router(endpoint.router)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
    
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import endpoint

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with specific origins allowed to access your API
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


# Mount the router
app.include_router(endpoint.router)