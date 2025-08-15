from fastapi import HTTPException, UploadFile

CONTENT_TYPE_MAP = {
    "mp3": "audio/mpeg",
    "wav": "audio/wav",
    "m4a": "audio/m4a",
    "mp4": "audio/mp4",
    "webm": "audio/webm",
    "ogg": "audio/ogg",
    "flac": "audio/flac",
    "aac": "audio/aac",
    "opus": "audio/opus",
}


def get_content_type(file: UploadFile) -> str:
    filename = file.filename or ""

    if "." in filename:
        ext = filename.rsplit(".", 1)[-1].lower()
        if ext in CONTENT_TYPE_MAP:
            return CONTENT_TYPE_MAP[ext]

    if file.content_type and file.content_type.startswith("audio/"):
        return file.content_type

    raise HTTPException(status_code=415, detail="Unsupported or unknown audio type")
