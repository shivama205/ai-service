from fastapi import APIRouter

from api.routers import project_management, pull_request

router = APIRouter(prefix="/api/v1")

router.include_router(pull_request.router)
router.include_router(project_management.router)

@router.get("/health", tags=[""])
async def health_check():
    return {
        "status": 200,
        "msg": "ok"
    }
