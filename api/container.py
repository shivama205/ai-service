from dependency_injector import containers, providers

from infrastructure.repositories.jira import JiraRepository
from infrastructure.repositories.llm import LLMRepository
from models.llm.openai import ChatModel
from services.project_management import ProjectManagementService
from services.pull_requests import PullRequestService

# from infrastructure.databases.mysql import MysqlDatabase


class Container(containers.DeclarativeContainer):
    # https://python-dependency-injector.ets-labs.org/examples/fastapi-sqlalchemy.html#container
    wiring_config = containers.WiringConfiguration(packages=["api.routers"])
    
    # Configuration
    config = providers.Configuration(yaml_files=["config.yml"])

    # Database
    # db = providers.Singleton(MysqlDatabase, db_url=config.db.url)

    # Models
    chat_model = providers.Factory(ChatModel, model_name=config.llm.model_name, api_key=config.llm.api_key)

    # Repositories
    jira_repository = providers.Factory(JiraRepository, api_url=config.jira.api_url, username=config.jira.username, password=config.jira.password)
    llm_repository = providers.Factory(LLMRepository, chat_model=chat_model, prompts=config.llm.prompts)

    # Services
    pr_service = providers.Factory(PullRequestService)
    project_service = providers.Factory(ProjectManagementService, jira_repository=jira_repository, llm_repository=llm_repository)
