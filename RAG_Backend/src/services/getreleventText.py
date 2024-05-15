from qdrant_client import QdrantClient
import google.generativeai as gemini_client

def generate_context(question: str, collection_name, qdrant_client: QdrantClient) -> str:
    try:
        """
        Generate context based on the question by retrieving relevant text from Qdrant.
        """
        # Look for Relevant Text in Qdrant
        results = qdrant_client.search(
            collection_name=collection_name,
            query_vector=gemini_client.embed_content(
                model="models/embedding-001",
                content=question,
                task_type="retrieval_query",
            )["embedding"],
        )

        # Extract text content from each result
        text_contents = []
        for result in results:
            content = {
                "id": result.id,
                "version": result.version,
                "score": result.score,
                "payload": result.payload,
                "vector": result.vector,
                "shard_key": result.shard_key
            }
            text_content = content['payload']['text']
            text_contents.append(text_content)
        
        context = "\n".join(text_contents)
        return context
    
    except Exception as e:
        # Handle any errors that occur during the execution
        print(f"An error occurred while generating context: {str(e)}")
        return ""
