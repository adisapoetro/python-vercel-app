from fastapi import FastAPI
from datetime import datetime
from typing import Dict

app = FastAPI(
    title="My Awesome API",
    description="A beautiful and feature-rich API",
    version="1.0.0"
)

@app.get("/api/hello")
async def hello() -> Dict:
    return {
        "message": "Hello from Python on Vercel!",
        "timestamp": datetime.now().isoformat(),
        "status": "success",
        "data": {
            "greeting": "Welcome to our beautiful API",
            "features": [
                "Fast responses",
                "Clean JSON structure",
                "Type hints",
                "Auto-documentation"
            ]
        }
    }

@app.get("/")
async def root() -> Dict:
    return {
        "status": "online",
        "service": "My Awesome API",
        "endpoints": [
            "/api/hello",
            "/docs",
            "/redoc"
        ]
    }
