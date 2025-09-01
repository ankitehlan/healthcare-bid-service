import numpy as np
from typing import List


class Retriever:
    """
    Mock Retriever class to simulate Retrieval-Augmented Generation (RAG).
    Instead of using a real embedding model (like OpenAI embeddings) or a
    vector database (FAISS/ChromaDB), this uses random vectors to mimic
    embeddings and cosine similarity to find "similar" bids.
    """

    def __init__(self):
        # List of mock stored bids in your "knowledge base"
        self.mock_bids = [
            "Healthcare service for elderly care",
            "Emergency room staffing request",
            "Telemedicine consultation package",
        ]

        # Create random mock embeddings for each stored bid
        # Here, each bid is represented as a 5-dimensional vector
        np.random.seed(42)  # Fixed seed for reproducibility
        self.embeddings = np.random.rand(len(self.mock_bids), 5)

    def _embed(self, text: str) -> np.ndarray:
        """
        Generate a fake embedding vector for a given text.

        In a real implementation, this would use a model like OpenAI's
        `text-embedding-ada-002` or similar. Here, we simulate embeddings
        with random vectors based on the text hash to ensure consistency.
        """
        np.random.seed(abs(hash(text)) % (10**6))  # Seed based on text hash
        return np.random.rand(5)  # 5-dimensional random vector

    def find_similar_bids(self, bid_request: str, top_k: int = 2) -> List[str]:
        """
        Find the top_k most similar stored bids to the given bid_request.

        Args:
            bid_request (str): The new incoming healthcare bid text.
            top_k (int): Number of similar bids to return.

        Returns:
            List[str]: A list of similar bids from the knowledge base.
        """
        # Get a mock embedding for the input bid request
        query_vec = self._embed(bid_request)

        # Compute cosine similarity between query and stored embeddings
        similarities = self.embeddings @ query_vec / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_vec)
        )

        # Get indices of top_k most similar bids
        top_indices = np.argsort(similarities)[::-1][:top_k]

        # Return the corresponding bids
        return [self.mock_bids[i] for i in top_indices]
