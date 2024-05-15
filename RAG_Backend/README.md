# RAG Application

This RAG application harnesses data from a website, vectorizes it using Qdrant, a vector database, and employs Gemini AI to generate answers to user queries. By leveraging Qdrant's vectorization capabilities, the application efficiently retrieves relevant documents from the database when users submit questions via the endpoint facilitated by FASTAPI. Gemini AI then formulates responses based on the queried question and the pertinent texts or documents sourced from the vector database.

## Built With

### Dependencies

The application relies on the following dependencies, which need to be installed:

- [ipython](https://pypi.org/project/ipython/): Interactive Python environment.
- [google-generativeai](https://pypi.org/project/google-generativeai/): Google's Generative AI library.
- [qdrant-client](https://pypi.org/project/qdrant-client/): Client library for Qdrant, a vector database.
- [fastapi](https://pypi.org/project/fastapi/): FastAPI framework for building APIs with Python.
- [uvicorn[standard]](https://pypi.org/project/uvicorn/): ASGI server for running FastAPI applications.

Make sure to include these dependencies in your `requirements.txt` file:

```plaintext
ipython
google-generativeai
qdrant-client
fastapi
uvicorn[standard]
beautifulsoup4
numpy
```

## Installation

1. Clone the repository: `git clone https://github.com/Codekorefataifelbo/RAG-Gemini-Qdrant.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `docker compose up --build`

## Architecture

The RAG application is built on a robust architecture that seamlessly integrates various components for efficient processing of user queries:

1. **Data Collection**: The application gathers data from a website, extracting relevant textual information.

2. **Vectorization**: The collected data is vectorized and stored in Qdrant, a vector database, using the qdrant-client library. This process converts textual data into numerical vectors, enabling efficient retrieval and analysis.

3. **API Endpoint**: Utilizing FastAPI, the application exposes an endpoint where users can submit their queries.

4. **Question-Answering Engine**: When a query is received, the application leverages Gemini AI, a pre-trained language model, to generate accurate answers. Gemini AI dynamically examines the relevant textual documents stored in the vector database to provide comprehensive responses.

This architecture ensures a seamless flow of information retrieval and processing, delivering accurate and timely responses to user queries.

## Usage

To utilize the RAG application, follow these simple steps:

1. **Environment Setup**:
   - Create an environment file (`env`) and provide the necessary API keys for Gemini and Qdrant.

2. **Dockerization**:
   - This application has been containerized using Docker for seamless deployment.
   - Open the terminal in your VS Code editor and run the command `docker-compose up --build` to build and start the Docker containers.

3. **Access the Endpoint**:
   - Once the Docker containers are up and running, navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your web browser.
   - This will open the FastAPI documentation interface where you can try out the `/query` endpoint and submit your queries.

## Contributing

Contributions to the RAG application are welcome! To get started, fork the repository and submit a pull request.

