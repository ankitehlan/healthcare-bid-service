from fastapi import APIRouter
from schemas.bid_schemas import BidRequest, BidResponse
from services.bid_responder import BidResponder

router = APIRouter()
responder = BidResponder()

@router.post("/", response_model=BidResponse)
def get_bid_response(request: BidRequest):
    """
    Handle bid request and return mock AI responses with retrieval integration.
    """
    return responder.process_bid(request)
