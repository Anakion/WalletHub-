import toml
from pydantic import (BaseModel,
                      model_validator)

from pydantic_settings import (BaseSettings,
                               SettingsConfigDict)

from Cryptos.auth_service.app.core.path import (path_env_file,
                                                path_toml_file)


class EnvSettings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    POSTGRES_DB: str
    SECRET_KEY: str
    PATH_DB: str


    model_config = SettingsConfigDict(
        env_file=path_env_file, env_file_encoding="utf-8", extra="ignore"
    )

class TOMLSettings(BaseModel):
    PROJECT_NAME: str
    VERSION: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str
    REDIS_HOST: str
    REDIS_PORT: int


    @classmethod
    def load_from_toml(cls, path: str = None) -> "TOMLSettings":
        if path is None:
            path = path_toml_file
        # Loading data from config.toml
        config_data = toml.load(path)
        # Returning a class object with the passed values
        return cls(
            PROJECT_NAME=config_data["auth_service"]["PROJECT_NAME"],
            VERSION=config_data["auth_service"]["VERSION"],
            ACCESS_TOKEN_EXPIRE_MINUTES=config_data["auth_service"]["ACCESS_TOKEN_EXPIRE_MINUTES"],
            JWT_ALGORITHM=config_data["security"]["JWT_ALGORITHM"],
            REDIS_HOST=config_data["redis"]["REDIS_HOST"],
            REDIS_PORT=config_data["redis"]["REDIS_PORT"],
        )


# Union class
class Settings(EnvSettings):
    toml_settings: TOMLSettings

    @model_validator(mode="before")
    def load_toml(cls, values):
        # Loading settings from a TOML file
        toml_settings = TOMLSettings.load_from_toml()
        values['toml_settings'] = toml_settings
        return values


settings = Settings()
print(settings.SECRET_KEY)





