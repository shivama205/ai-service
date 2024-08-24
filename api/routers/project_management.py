from typing import Annotated
from fastapi import APIRouter
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path

from api.container import Container
from services.project_management import ProjectManagementService

router = APIRouter(
    prefix="",
    tags=["Project Management"],
)


@router.get("/filters/{filter_id}/daily-summary")
@inject 
async def get_daily_summary(
    filter_id: Annotated[str, Path(title="The ID of the issue filter")],
    project_service: ProjectManagementService = Depends(Provide[Container.project_service]),
):
    return project_service.get_daily_summary(filter_id=filter_id)