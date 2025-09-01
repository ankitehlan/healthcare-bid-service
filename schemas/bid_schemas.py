from pydantic import BaseModel
from typing import Optional

class BidRequest(BaseModel):
    bid_request: str
    context: Optional[str] = None

class BidResponse(BaseModel):
    gemini_answer: str
    custom_llm_expected_answer: str
