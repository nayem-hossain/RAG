import qdrant_client  # Client for Qdrant, a vector database
import google.generativeai as genai  # Generative AI library for Gemini API
from qdrant_client import QdrantClient  # Qdrant client for interacting with Qdrant database
from config.settings import genaimodel
from services.getreleventText import generate_context

def generate_answer(
    question: str,
    collection_name,
    qdrant_client: QdrantClient,
    n_points: int = 5,
    conversation_history: list = [],
):
    try:
        # Call the generate_context function to get the context
        context = generate_context(question, collection_name, qdrant_client)

        # Create the conversation history with the current question
        conversation_history.append(f"Question: {question.strip()}")

        # Create the metaprompt with conversation history and context
        metaprompt = f""" 
        You are a helpful assistant for Gigalogy Company, dedicated to providing accurate and relevant information within the context provided. 
        Please aim for answers between 100-200 words, prioritizing helpfulness and accuracy. If a question falls outside the 'Context' given, 
        first look for the closest match in the context and if that makes sense use that or else avoid providing inaccurate information. 
        Instead, politely indicate that the question is beyond the scope of the provided context.
        
        Conversation History:
        {"\n".join(conversation_history)}

        Context: {context}

        Answer: """

        # Generate the response using the Gemini model with conversational memory
        response = genaimodel.generate_content(
            metaprompt, model="models/conversational-memory-001"
        )

        # Remove markdown syntax from the response text
        response_text = response.text.replace("**", "").replace("*", "").replace("`", "")

        # Replace double newlines with single newline
        response_text = response_text.replace("\n\n", "\n")

        # Remove extra spaces and leading/trailing spaces
        response_text = response_text.strip()

        # Append the response to the conversation history
        conversation_history.append(f"Answer: {response_text}")

        return response_text
    except Exception as e:
        # Handle any errors that occur during the execution
        print(f"An error occurred while generating answer: {str(e)}")
        return ""