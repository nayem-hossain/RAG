import os
import qdrant_client
from qdrant_client import QdrantClient
from qdrant_client.models import CollectionDescription
from dotenv import load_dotenv
from models.qdrant_setup_v2 import add_documents_to_collection
from config.settings import qdrant_client

# Load environment variables from .env file
load_dotenv()

from qdrant_client import QdrantClient

def check_and_add_collection(collection_name: str):
    """
    Check if the collection already exists.
    If it does not exist, add documents to the collection.
    """
    try:
        existing_collections = qdrant_client.get_collections()
        collection_names = [collection.name for collection in existing_collections.collections]
        
        if collection_name in collection_names:
            print(f"Collection '{collection_name}' already exists. Skipping adding documents to the collection.")
        else:
            add_documents_to_collection(collection_name, qdrant_client)
    except Exception as e:
        print(f"An error occurred while checking or adding collection '{collection_name}': {str(e)}")

