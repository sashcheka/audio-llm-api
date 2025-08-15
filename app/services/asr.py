import httpx

from app.core.settings import settings
from app.schemas.asr import ASRResponse


async def transcribe_audio(audio_bytes: bytes, content_type: str) -> str:
    """
    Send audio bytes to Whisper (via HF router) and return plain text.
    """
    headers = {
        "Authorization": f"Bearer {settings.hf_token}",
        "Content-Type": content_type,
    }

    URL = f"{settings.asr_url_base}/{settings.asr_model}"
    async with httpx.AsyncClient(timeout=settings.request_timeout_seconds) as client:
        response = await client.post(URL, headers=headers, content=audio_bytes)

    try:
        data: ASRResponse = response.json()
    except Exception as e:
        raise RuntimeError(f"ASR non-JSON response: {e}") from e

    if response.is_success and isinstance(data, dict) and "text" in data:
        return data["text"]

    raise RuntimeError(f"ASR failed (status {response.status_code}): {data}")
