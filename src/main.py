from fastapi import FastAPI
import uvicorn

from core.config import server_config


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=server_config.host,
        port=server_config.port,
        reload=server_config.reload)
