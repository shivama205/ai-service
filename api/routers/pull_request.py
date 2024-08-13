from typing import Annotated
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path

from api.container import Container
from services.pull_requests import PullRequestService

router = APIRouter(
    prefix="",
    tags=["PullRequest", "PR"],
)


@router.post("/pr/{pr-id}/review")
@inject
async def review_code(
    pr_id: Annotated[str, Path(title="The ID of pull request to be reviewed")],
    pr_service: PullRequestService = Depends(Provide[Container.pr_service]),
):
    return pr_service.review_code(pr_id=pr_id)
