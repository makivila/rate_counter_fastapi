from os import environ as env


class Config:
    DB_USER: str = env["DB_USER"]
    DB_PASSWORD: str = env["DB_PASSWORD"]
    DB_DATABASE_NAME: str = env["DB_DATABASE_NAME"]
    DB_PORT: int = env["DB_PORT"]
    DB_HOST: int = env["DB_HOST"]
