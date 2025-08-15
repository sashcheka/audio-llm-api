from typing import List, TypedDict


class Message(TypedDict):
    content: str


class Choice(TypedDict):
    message: Message


class LLMResponse(TypedDict):
    choices: List[Choice]
