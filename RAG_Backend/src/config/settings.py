import os
from dotenv import load_dotenv
import google.generativeai as genai
import google.generativeai as gemini_client
from qdrant_client import QdrantClient

# Load environment variables from .env file
load_dotenv()

# Define the paths to the secret files
GEMINI_API_KEY_FILE = "/run/secrets/gemini_api_key"
QDRANT_URL_FILE = "/run/secrets/qdrant_url"
QDRANT_API_KEY_FILE = "/run/secrets/qdrant_api_key"

# Read the API keys and other configuration variables from the secret files
with open(GEMINI_API_KEY_FILE, "r") as file:
    GEMINI_API_KEY = file.read().strip()

with open(QDRANT_URL_FILE, "r") as file:
    QDRANT_URL = file.read().strip()

with open(QDRANT_API_KEY_FILE, "r") as file:
    QDRANT_API_KEY = file.read().strip()

# Configure the Gemini API key
gemini_client.configure(api_key=GEMINI_API_KEY)

# Initialize the generative model for Gemini
genaimodel = genai.GenerativeModel('gemini-pro')

# Initialize the Qdrant client
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)
