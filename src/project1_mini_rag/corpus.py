"""Day 02 — 30 short text snippets about LLM engineering topics."""

SNIPPETS = [
    # --- What is an LLM? ---
    "A large language model (LLM) is a neural network trained on vast amounts of text to predict the next token.",
    "LLMs like GPT-4, Gemini, and Claude learn statistical patterns in language from books, websites, and code.",
    "The transformer architecture, introduced in 2017, is the backbone of virtually every modern LLM.",
    "Tokens are the atomic units LLMs process — a token is roughly 3–4 characters or about 0.75 words.",
    "The context window is the maximum number of tokens an LLM can see at once; exceeding it loses earlier text.",

    # --- Embeddings ---
    "An embedding is a dense numerical vector that encodes the semantic meaning of a piece of text.",
    "Sentence-transformers are small, CPU-friendly models that produce high-quality sentence embeddings.",
    "Cosine similarity measures the angle between two vectors — values near 1.0 mean semantically close.",
    "Embedding models map text into a high-dimensional space where similar concepts cluster together.",
    "The all-MiniLM-L6-v2 model produces 384-dimensional embeddings and runs fast on CPU.",

    # --- RAG basics ---
    "Retrieval-Augmented Generation (RAG) grounds LLM answers in a retrieved set of relevant documents.",
    "RAG reduces hallucinations by giving the model factual context at inference time rather than relying on memorized weights.",
    "A RAG pipeline has two phases: offline indexing (embed documents) and online retrieval (embed query, find nearest).",
    "Semantic search finds documents whose meaning is close to the query, not just ones that share keywords.",
    "Chunking splits long documents into smaller passages so each chunk fits in the context window.",

    # --- Vector databases ---
    "A vector database stores embeddings and supports efficient approximate nearest-neighbour (ANN) queries.",
    "Chroma is a lightweight, open-source vector database that runs locally with no server required.",
    "FAISS, Qdrant, Pinecone, and Weaviate are popular vector stores that scale to billions of vectors.",
    "An index stores pre-computed embeddings so you never have to re-embed the same document twice.",
    "Cosine similarity and dot-product distance are the two most common metrics used in vector search.",

    # --- LangChain / LangGraph ---
    "LangChain provides abstractions for chains, retrievers, and memory to speed up LLM app development.",
    "LCEL (LangChain Expression Language) lets you compose chains with the pipe operator for readable code.",
    "LangGraph models stateful agent workflows as directed graphs — nodes are functions, edges are transitions.",
    "A tool in LangGraph is a function the agent can call to interact with the outside world (search, code, APIs).",
    "Memory in a conversational agent stores prior turns so the model can refer back to earlier context.",

    # --- Evaluation ---
    "Ragas is an open-source framework for evaluating RAG pipelines using metrics like faithfulness and relevancy.",
    "Faithfulness measures whether the answer is grounded in the retrieved context, not just plausible-sounding.",
    "Answer relevancy scores how directly the generated answer addresses the user's question.",
    "Context recall checks whether the retrieved chunks actually contain the information needed to answer.",
    "LLM-as-a-judge uses a strong model to score another model's output — fast and surprisingly reliable at scale.",
]
