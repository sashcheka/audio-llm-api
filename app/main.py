from fastapi import Depends, FastAPI, File, HTTPException, UploadFile

from app.core.auth import verify_api_key
from app.schemas.audio import AudioProcessResponse
from app.services.asr import transcribe_audio
from app.services.llm import generate_reply
from app.services.utils import get_content_type

app = FastAPI()


@app.post(
    "/process", summary="Upload an audio file to transcribe and get a short answer"
)
async def process(
    file: UploadFile = File(...), _: bool = Depends(verify_api_key)
) -> AudioProcessResponse:
    """
    Upload an audio file (mp3).
    Returns:
      - transcript: text from Whisper
      - answer: one short sentence from LLM
    """
    audio_bytes = await file.read()
    if not audio_bytes:
        raise HTTPException(status_code=400, detail="Empty file")

    try:
        content_type = get_content_type(file)
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"This audio file type is not supported: {e}"
        )

    try:
        transcript = await transcribe_audio(audio_bytes, content_type)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"ASR error: {e}")

    prompt = f"What do you think about this: {transcript}"
    try:
        answer = await generate_reply(prompt)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM error: {e}")

    return AudioProcessResponse(transcript=transcript, answer=answer)
