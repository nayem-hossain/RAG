from qdrant_client.models import PointStruct, VectorParams, Distance
import google.generativeai as gemini_client
import os
import qdrant_client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def add_documents_to_collection(collection_name, qdrant_client):
    try:
        # Get the path to the root directory
        root_dir = os.path.dirname(os.path.abspath(__file__))
        text_files_dir = os.path.join(root_dir, "scraped_data")
        
        # Read all the .txt files from the text_files folder
        documents = []
        for filename in os.listdir(text_files_dir):
            if filename.endswith(".txt"):
                file_path = os.path.join(text_files_dir, filename)
                with open(file_path, "r") as file:
                    document = file.read()
                    documents.append(document)

        # Remove any leading or trailing whitespace from the lines
        documents = [doc.strip() for doc in documents]

        # Embed documents using gemini_client
        results = [
            gemini_client.embed_content(
                model="models/embedding-001",
                content=document,
                task_type="retrieval_document",
                title="Qdrant x Gemini",
            )
            for document in documents
        ]

        # Creating Qdrant Points
        points = [
            PointStruct(
                id=idx,
                vector=response['embedding'],
                payload={"text": document},
            )
            for idx, (response, document) in enumerate(zip(results, documents))
        ]

        # Create Collection
        qdrant_client.create_collection(collection_name, vectors_config=
        VectorParams(
            size=768,
            distance=Distance.COSINE,
            )
        )
        
        # Add to Collection
        qdrant_client.upsert(collection_name, points)
        
        print("Documents added successfully to the collection.")
    
    except Exception as e:
        print(f"An error occurred while setting up qdrant collection")
        
        
# add_documents_to_collection("Gigalogy Data", qdrant_client)