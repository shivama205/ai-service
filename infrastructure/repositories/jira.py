from typing import List
import requests
from requests.auth import HTTPBasicAuth as TPBasicAuth

from models.schemas.jira_issue import JiraIssue
from logger import logger

class JiraRepository:
    def __init__(self, api_url: str, username: str, password: str) -> None:
        self.api_url = api_url
        self.auth = TPBasicAuth(
            username=username,
            password=password
        )

    def get_issues_from_filter(self, filter_id: int) -> List[JiraIssue]:
        endpoint = f"{self.api_url}/search"

        headers = { "Accept": "application/json" }

        query_params = {
            "jql": f"filter={filter_id}",
        }

        response = requests.get(
            url=endpoint,
            headers=headers,
            params=query_params,
            auth=self.auth
        )
        response.raise_for_status()

        return self._serialize_issues(response.json())

    def _serialize_issues(self, data: dict) -> List[JiraIssue]:

        issues = data.get("issues", [])
        jira_issues: List[JiraIssue] = []

        for issue in issues:

            project = issue.get("fields", {}).get("parent", {}).get("fields", {}).get("summary", "")
            start_date = issue.get("fields", {}).get("customfield_10025", "")
            due_date = issue.get("fields", {}).get("duedate", "")

            jira_issue = JiraIssue(
                key=issue["key"],
                type=issue["fields"]["issuetype"]["name"],
                summary=issue["fields"]["summary"],
                project=project,
                reporter=issue["fields"]["reporter"]["displayName"],
                assignee=issue["fields"]["assignee"]["displayName"],
                status=issue["fields"]["status"]["name"],
                start_date=start_date,
                due_date=due_date
            )

            jira_issues.append(jira_issue)

        return jira_issues