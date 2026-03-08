## Semantic Search System with Fuzzy Clustering and Semantic Cache

This project was built as part of the Trademarkia AI/ML Engineer assignment.

The goal of this project is to design a lightweight semantic search system that understands the meaning of user queries, rather than relying on simple keyword matching.

The system is built using the 20 Newsgroups dataset, which contains around 20,000 documents across multiple discussion topics.

The project focuses on three core ideas:

*Representing documents using vector embeddings
*Discovering semantic structure using fuzzy clustering
*Reducing redundant computation using a semantic cache

The system is exposed through a FastAPI service.

## 1. Project Overview

Traditional search systems rely on keyword matching, which often fails when similar queries are phrased differently.

For example:

"space exploration missions"
"future missions to space"

Even though both queries have the same meaning, a keyword-based system may treat them as unrelated queries.

This project solves that problem by converting both documents and queries into vector embeddings, allowing similarity comparison based on semantic meaning.

## 2. Dataset

The project uses the 20 Newsgroups dataset, which contains approximately 20,000 posts across 20 different categories, including:technology ,politics ,sports ,science

Preprocessing Steps

Before generating embeddings, the dataset was cleaned by:
*Removing email headers
*Removing signatures
*Removing unnecessary formatting
This ensures that only meaningful text content is used for embedding and clustering.

## 3. Embeddings and Vector Search

Each document is converted into a dense vector representation using the Sentence Transformers library.

Model Used: all-MiniLM-L6-v2
Model Characteristics:384-dimensional embeddings , Lightweight and fast ,Strong semantic similarity performance

Embedding Pipeline:
Document Text
      ↓
Sentence Transformer
      ↓
384-dimensional vector

The generated embeddings are stored using FAISS, which enables efficient similarity search across large vector collections.

FAISS allows the system to quickly retrieve documents that are semantically similar to a user query.

## 4. Fuzzy Clustering

Although the dataset contains predefined categories, real-world topics often overlap.

For example, a document discussing gun policy may belong to both:

politics

firearms discussions

To capture this behavior, the project uses Fuzzy C-Means clustering.

Why Fuzzy Clustering?

Unlike traditional clustering, fuzzy clustering assigns probabilities instead of fixed labels.


## 5. Semantic Cache

A traditional cache only works when the exact same query is repeated.

However, users often ask similar questions using different wording.

To address this problem, a semantic cache was implemented.

Cache Workflow

i.The query is converted into an embedding.

ii.The embedding is compared with embeddings of previous queries stored in the cache.

iii. If similarity exceeds a threshold → cached result is returned.

iv.Otherwise → the query is processed normally and stored in the cache.

Benefit: This allows the system to reuse results for semantically similar queries, significantly reducing repeated computation.

## 6. API Service
<img width="1801" height="474" alt="image" src="https://github.com/user-attachments/assets/cadd03ca-8275-4fe9-97d1-f3da4aec3a98" />

The system is exposed through a FastAPI service.

Once the server is running, the API documentation can be accessed at:

http://localhost:8000/docs

The following endpoints are available.

## 7. API Endpoints
POST /query

This endpoint accepts a natural language query and returns the most relevant documents.

Example Request
{
  "query": "space exploration missions"
}
Example Response
<img width="1614" height="504" alt="image" src="https://github.com/user-attachments/assets/8e5e8817-daaa-4567-9eff-c5216e197624" />

The response also indicates whether the result was retrieved from the semantic cache.

GET /cache/stats

Returns statistics about the current cache state.

Example output:

<img width="188" height="189" alt="image" src="https://github.com/user-attachments/assets/104a8d8d-90f2-4e61-a6ae-3ffce9a6243b" />

This includes:
total cache entries,
cache hits,
cache misses,
hit rate

DELETE /cache

<img width="572" height="122" alt="image" src="https://github.com/user-attachments/assets/1ca1aa23-3abb-404a-93f1-2340243dbd0c" />

This endpoint clears all cache entries and resets the statistics.


## 8. Docker Support   {Bonus Dockerisation task}

The project includes a Dockerfile, allowing the entire application to be containerized.This ensures the service can run consistently across different environments.

## Running with Docker


Build the  docker image: docker build -t semantic-search-api .
<img width="1600" height="534" alt="image" src="https://github.com/user-attachments/assets/057e8c71-9242-40bb-a334-6b1c99340c4f" />



Run the docker  container: docker run -p 8000:8000 semantic-search-api
<img width="1855" height="607" alt="image" src="https://github.com/user-attachments/assets/33b9de89-1852-4964-bc67-d550a7d02355" />


The API will be available at: http://localhost:8000/docs
<img width="1756" height="782" alt="image" src="https://github.com/user-attachments/assets/9ec90b78-892d-4354-a776-1e57d98e45ad" />

## Running with Docker Compose .yaml
In addition to the Dockerfile, the project also includes a docker-compose.yml file.
Docker Compose simplifies container orchestration and allows the service to be started with a single command.
Start the Service Using Docker Compose- docker compose up --build
<img width="577" height="322" alt="image" src="https://github.com/user-attachments/assets/d09ed127-4c99-41b6-a4ff-aedc4cdafc23" />


Docker Compose will:

Build the Docker image : trademarkia_semantic_search-semantic-search
<img width="1848" height="635" alt="image" src="https://github.com/user-attachments/assets/9999931a-d340-4d37-95ae-d7fb9ef649ed" />


Create the container : trademarkia_semantic_search
<img width="1856" height="592" alt="image" src="https://github.com/user-attachments/assets/637503a5-7b69-469f-a35a-b60491afccac" />


Start the FastAPI service automatically

<img width="922" height="183" alt="image" src="https://github.com/user-attachments/assets/54eaf041-c182-4b21-8b4b-737852312dea" />
The API can again be accessed at: http://localhost:8000/docs


## Now Bonus Dockerisation task:
<img width="675" height="297" alt="image" src="https://github.com/user-attachments/assets/07aa608b-5679-4bf5-b9b2-993019002b9a" />


*the service runs inside Docker

*FastAPI is exposed on port 8000

*Additionally, a docker-compose configuration is provided to simplify container orchestration and startup {docker-compose.yml}.

*the semantic search system loads the FAISS index and embedding model on startup

9. Final Notes

This project demonstrates how semantic embeddings, fuzzy clustering, and caching can be combined to build a more intelligent search system.

Instead of relying on exact keyword matching, the system retrieves results based on semantic meaning, making the search process more flexible and efficient.

The semantic cache further improves performance by avoiding repeated computations for similar queries.














