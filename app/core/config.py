from pydantic import BaseSettings

class Settings(BaseSettings):
    project_name: str = "Data Preparation API"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
