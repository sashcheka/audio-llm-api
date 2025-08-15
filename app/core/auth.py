from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

from app.core.settings import settings

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def verify_api_key(api_key: str = Security(api_key_header)) -> bool:
    if api_key and api_key == settings.api_key:
        return True
    raise HTTPException(status_code=401, detail="Invalid or missing API key")
