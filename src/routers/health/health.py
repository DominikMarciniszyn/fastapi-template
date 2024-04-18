"""Health check router for the service. It contains liveness and readiness."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/liveness", tags=["health"])
async def healthcheck() -> dict[str, str]:
    """Liveness check for the service."""

    return {"status": "ok"}
