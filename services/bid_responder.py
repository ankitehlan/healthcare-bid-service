from schemas.bid_schemas import BidRequest, BidResponse
from retrieval.retriever import Retriever


class BidResponder:
    """
    Handles AI bidding logic, simulates a base Gemini answer,
    and applies a custom enhancement layer.
    """

    def __init__(self):
        self.retriever = Retriever()

    def process_bid(self, request: BidRequest) -> BidResponse:
        """
        Process a bid request and return both a Gemini (mock) answer
        and an enhanced custom answer.
        """
        # Simulate Gemini answer
        gemini_answer = f"Gemini suggestion for: {request.bid_request}"

        # Simulate enhanced answer (uses context if available)
        custom_answer = (
            f"Enhanced answer using context: {request.context or 'No context provided'}"
        )

        # Retrieve similar bids
        similar_bids = self.retriever.find_similar_bids(request.bid_request)

        # (Optional) Add retrieved bids info to custom answer
        if similar_bids:
            custom_answer += f". Similar past bids: {', '.join(similar_bids)}"

        return BidResponse(
            gemini_answer=gemini_answer,
            custom_llm_expected_answer=custom_answer,
        )
