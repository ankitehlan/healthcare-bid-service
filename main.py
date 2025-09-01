from fastapi import FastAPI
from routes import bid_routes

app = FastAPI(
    title="Healthcare Bid Service",
    description="A FastAPI microservice for processing healthcare bids with AI logic",
    version="1.0.0",
)

# Include the bid response routes
app.include_router(bid_routes.router, prefix="/bid-response", tags=["Bids"])


@app.get("/")
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "service": "Healthcare Bid Service"}
