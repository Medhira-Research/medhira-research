"""The first API for Medhira Research.

Start small: understand every line before adding features.
"""
from fastapi import FastAPI

app = FastAPI(
    title="Medhira Research API",
    description="The backend for the Medhira Research learning and collaboration platform.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    """Return a welcome message from the API."""
    return {
        "message": "Medhira API is alive.",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    """A simple endpoint that deployment systems can use to check the API."""
    return {"status": "ok"}
