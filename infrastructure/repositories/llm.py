import json
from typing import Dict, List

from models.llm.openai import ChatModel
from models.schemas.jira_issue import JiraIssue


class LLMRepository:
    def __init__(self, chat_model: ChatModel, prompts: Dict):
        self.chat_model = chat_model
        self.prompts = prompts

    def summarize_issues(self, issues: List[JiraIssue]):
        prompt = self.prompts.get("SUMMARIZE_ISSUES_PROMPT", "")
        response = self.chat_model.chat(
            system_prompt=prompt,
            human_message=str(issues)
        )

        return response.get("content", "")

        
