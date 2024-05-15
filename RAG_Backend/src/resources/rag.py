import qdrant_client  # Client for Qdrant, a vector database
import google.generativeai as genai  # Generative AI library for Gemini API
from qdrant_client import QdrantClient  # Qdrant client for interacting with Qdrant database
from config.settings import genaimodel
from services.getreleventText import generate_context


def generate_answer(question: str, collection_name, qdrant_client: QdrantClient, n_points: int = 5) -> str:
    try:
        # Call the generate_context function to get the context
        context = generate_context(question, collection_name, qdrant_client)

        # Create Metaprompt to pass to Gemini
        metaprompt = f"""
        You are a helpful assistant for Gigalogy Company, dedicated to providing accurate and relevant information within the context provided. Please aim for answers between 100-200 words, prioritizing helpfulness and accuracy.

        If a question falls outside the 'Context' given, first look for the closest match in the context and if that makes sense use that or else avoid providing inaccurate information. Instead, politely indicate that the question is beyond the scope of the provided context.

        Question: {question.strip()}

        Context:
        {context}

        Answer:
        """

        # print(context)
        
        response = genaimodel.generate_content(metaprompt)

        # # Remove markdown syntax from the response text
        # response_text = response.text.replace("**", "").replace("*", "").replace("`", "")

        # # Replace double newlines with single newline
        # response_text = response_text.replace("\n\n", "\n")

        # # Remove extra spaces and leading/trailing spaces
        # response_text = response_text.strip()

        return response.text
    
    except Exception as e:
        # Handle any errors that occur during the execution
        print(f"An error occurred while generating answer: {str(e)}")
        return ""


    

