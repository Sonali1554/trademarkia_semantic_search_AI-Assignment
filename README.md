Semantic Search System with Fuzzy Clustering and Semantic Cache

This project was built as part of the Trademarkia AI/ML Engineer assignment.
The goal was to design a lightweight semantic search system that can understand the meaning of user queries instead of relying on exact keyword matching.

The system works on the 20 Newsgroups dataset, which contains around 20,000 documents across different discussion topics. The project focuses on three main ideas:

Representing documents using vector embeddings

Discovering semantic structure using fuzzy clustering

Reducing redundant computation using a semantic cache

A FastAPI service is used to expose the system through a simple API.

Project Overview

Traditional search systems rely on keyword matching. This means two queries that mean the same thing but are written differently may return different results.

For example:

"space exploration missions"

"future missions to space"

Both queries have very similar meaning, but a keyword-based system might treat them as different queries.

This project solves that problem by converting both documents and queries into vector embeddings, allowing the system to compare them based on semantic similarity.

Dataset

The project uses the 20 Newsgroups dataset, which contains roughly 20,000 posts across 20 categories such as technology, politics, sports, and science.

Before processing, the dataset was cleaned to remove unnecessary metadata such as headers and formatting so that only the relevant text content was used for embedding and clustering.

Embeddings and Vector Search

Each document is converted into a dense vector representation using the Sentence Transformers library.

The model used is:

all-MiniLM-L6-v2

This model produces a 384-dimensional embedding vector for each document. These vectors capture the semantic meaning of the text.

Once the embeddings are generated, they are stored using FAISS, which is a library designed for efficient similarity search over large collections of vectors.

This allows the system to quickly retrieve documents that are semantically similar to a user query.

Fuzzy Clustering

The dataset already contains labeled categories, but real-world topics often overlap.

For example, a document discussing gun policy may belong to both politics and firearms discussions.

To capture this behavior, the project uses Fuzzy C-Means clustering instead of traditional clustering.

Unlike hard clustering, fuzzy clustering assigns each document a probability distribution across clusters.

Example:

Document A
Cluster 3 → 0.60
Cluster 7 → 0.25
Cluster 11 → 0.15

This means the document primarily belongs to cluster 3 but also shares characteristics with other clusters.

This approach better reflects the real semantic structure of the dataset.

Semantic Cache

A traditional cache only works if the exact same query is repeated.

However, users often ask similar questions in different ways. To address this, a semantic cache was implemented.

When a query is received:

The query is converted into an embedding.

The embedding is compared with embeddings of previous queries stored in the cache.

If the similarity is above a certain threshold, the cached result is returned.

Otherwise, the query is processed normally and the result is stored in the cache.

This approach allows the system to reuse results for semantically similar queries, improving efficiency.

API Service
<img width="1801" height="474" alt="image" src="https://github.com/user-attachments/assets/cadd03ca-8275-4fe9-97d1-f3da4aec3a98" />


The system is exposed through a FastAPI service.

Once the server is running, the API documentation can be accessed at:

http://localhost:8000/docs

The following endpoints are available.

POST /query

This endpoint accepts a natural language query and returns the most relevant documents.

Example request:

{
  "query": "space exploration missions"
}

Example response:

<img width="1614" height="504" alt="image" src="https://github.com/user-attachments/assets/8e5e8817-daaa-4567-9eff-c5216e197624" />


The response also indicates whether the result was retrieved from the semantic cache.

GET /cache/stats

Returns statistics about the current cache state.

Example output:

<img width="188" height="189" alt="image" src="https://github.com/user-attachments/assets/104a8d8d-90f2-4e61-a6ae-3ffce9a6243b" />

DELETE /cache
<img width="247" height="121" alt="image" src="https://github.com/user-attachments/assets/510aa172-7766-4efc-a6a9-af65b5403d81" />


Clears the cache and resets all statistics.

