"""Main module."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def healthcheck() -> dict[str, str]:
    """Health check endpoint."""

    return {"status": "ok"}
