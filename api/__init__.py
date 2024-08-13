from fastapi import APIRouter

from api.routers import pull_request

router = APIRouter(prefix="/api/v1")

router.include_router(pull_request.router)

@router.get("/health", tags=[""])
async def health_check():
    return {
        "status": 200,
        "msg": "ok"
    }
