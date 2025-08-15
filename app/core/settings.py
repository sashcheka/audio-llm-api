from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    hf_token: str = "default_hf_token"
    api_key: str = "default_api_key"
    asr_model: str = "default_asr_model"
    llm_model: str = "default_llm_model"
    asr_url_base: str = "https://router.huggingface.co/hf-inference/models"
    llm_url: str = "https://router.huggingface.co/v1/chat/completions"
    request_timeout_seconds: int = 60
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
