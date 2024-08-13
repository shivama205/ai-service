import uvicorn
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

import api
from api.container import Container
import api.routers
from logger import logger
from middleware import request_middleware


def create_app():
    logger.info("Starting API Server . . . ")
    app = FastAPI()

    container = Container()
    app.container = container

    # Uncomment the following lines to establish a database connection
    # db = container.db()
    # db.create_database()
    
    app.include_router(api.router)

    # add middleware
    app.add_middleware(BaseHTTPMiddleware, dispatch=request_middleware)

    return app

app = create_app()

if __name__ == "__main__":
    # For testing removed host as it compiles faster than host=0.0.0.0
    uvicorn.run("main:app", port=8080, reload=True)
