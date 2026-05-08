"""Health-related API routes.

Keeping routes in their own modules helps the project stay organized
as more endpoints are added.
"""

from fastapi import APIRouter

# APIRouter lets us group related endpoints together.
# Later, this can grow into larger feature-based route files.
router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """Basic health-check endpoint.

    Returns a simple status payload so humans, monitoring tools,
    or load balancers can quickly verify the API is running.
    """
    return {"status": "ok", "service": "mini-fintech-api"}
