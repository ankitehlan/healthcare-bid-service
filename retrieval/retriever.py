from typing import List


class Retriever:
    """
    Mock retriever that simulates similarity search.
    In a real-world scenario, you'd use FAISS or ChromaDB with embeddings.
    """

    def __init__(self):
        # Some mock past bids
        self.mock_bids = [
            "Healthcare service for elderly care",
            "Emergency room staffing request",
            "Telemedicine consultation package",
        ]

    def find_similar_bids(self, bid_request: str, top_k: int = 2) -> List[str]:
        """
        Return top_k mock bids that 'match' the input.
        This is a simple string filter for now.
        """
        matches = [bid for bid in self.mock_bids if bid_request.lower() in bid.lower()]
        return matches[:top_k]
