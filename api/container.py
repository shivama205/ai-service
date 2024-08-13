from dependency_injector import containers, providers

from services.pull_requests import PullRequestService

# from infrastructure.databases.mysql import MysqlDatabase


class Container(containers.DeclarativeContainer):
    # https://python-dependency-injector.ets-labs.org/examples/fastapi-sqlalchemy.html#container
    wiring_config = containers.WiringConfiguration(packages=["api.routers"])
    
    # Configuration
    # config = providers.Configuration(yaml_files=["config.yml"])

    # Database
    # db = providers.Singleton(MysqlDatabase, db_url=config.db.url)

    # Repositories

    # Services
    pr_service = providers.Factory(PullRequestService)
