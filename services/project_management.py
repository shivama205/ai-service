from typing import List
from infrastructure.repositories.jira import JiraRepository
from infrastructure.repositories.llm import LLMRepository
from models.schemas.jira_issue import JiraIssue


class ProjectManagementService:
    def __init__(self, jira_repository: JiraRepository, llm_repository: LLMRepository):
        self.jira_repository = jira_repository
        self.llm_repository = llm_repository

    def get_daily_summary(self, filter_id: str):
        issues: List[JiraIssue] = self.jira_repository.get_issues_from_filter(filter_id)

        # generate summary
        return self.llm_repository.summarize_issues(issues)

