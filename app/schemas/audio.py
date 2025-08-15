from pydantic import BaseModel


class AudioProcessResponse(BaseModel):
    transcript: str
    answer: str
