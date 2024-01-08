"""settings"""

from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["settings"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)

    is_true: bool


# HACK VS Code test explorer is suddenly complaining about settings. This sets up reasonable default values to use so that you can use the test explorer and interactive debugger.

settings = Settings(is_true=True)

settings = Settings()  # type: ignore
