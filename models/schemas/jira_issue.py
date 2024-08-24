from typing import Optional
from pydantic import BaseModel

class JiraIssue(BaseModel):
    key: str 
    type: str 
    summary: str 
    project: str 
    reporter: str 
    assignee: str
    status: str 
    start_date: Optional[str] = None
    due_date: Optional[str] = None

