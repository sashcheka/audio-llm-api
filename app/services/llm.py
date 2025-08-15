# app/services/llm.py
import httpx

from app.core.settings import settings
from app.schemas.llm import LLMResponse

SYSTEM_STYLE = (
    "You are concise and practical. "
    "Respond holistically in 1–2 sentences (max ~40 words) and end with a period. "
    "No preface, no lists, no emojis."
)


async def generate_reply(prompt: str) -> str:
    """
    Call chat completions and return a short, holistic answer string.
    """
    headers = {
        "Authorization": f"Bearer {settings.hf_token}",
    }
    payload = {
        "model": settings.llm_model,
        "messages": [
            {"role": "system", "content": SYSTEM_STYLE},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.5,
        "top_p": 0.7,
        "max_tokens": 100,
    }

    async with httpx.AsyncClient(timeout=settings.request_timeout_seconds) as client:
        resp = await client.post(settings.llm_url, headers=headers, json=payload)

    try:
        data: LLMResponse = resp.json()
        return data["choices"][0]["message"]["content"]
    except Exception:
        raise RuntimeError(f"LLM failed (status {resp.status_code}): {data}")
