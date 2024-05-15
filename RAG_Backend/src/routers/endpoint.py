from fastapi import APIRouter, HTTPException, Request
from config.settings import qdrant_client
from services.checkcollection import check_and_add_collection
from resources.rag import generate_answer

router = APIRouter()

# Call the function with the desired collection name
collection_name = "Gigalogy Data"

# Check if the collection exists and add documents if it doesn't
check_and_add_collection(collection_name)

@router.post("/query")
async def query_gemini_and_qdrant(request: Request):
    # Parse the JSON body of the request
    body = await request.json()
    question = body.get("question")
    print("this is request data",question)

    # Check if "question" field is provided in the request body
    if question is None:
        raise HTTPException(status_code=400, detail="Missing 'question' field in the request body")

    # Generate answer based on the question, collection name, and qdrant client
    response = generate_answer(question, collection_name, qdrant_client)
    
    
    return {"response": response}, 200