from app.config import Config
from fastapi import FastAPI
from app.router import router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(router)
register_tortoise(
    app=app,
    db_url=f"postgres://{Config.DB_USER}:{Config.DB_PASSWORD}"
    + f"@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_DATABASE_NAME}",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
