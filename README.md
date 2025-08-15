# Audio → Text + LLM API

A small FastAPI service that:
1. Accepts an audio file (`mp3`, `wav`, etc.).
2. Transcribes it to text using Hugging Face Whisper.
3. Generates a short, holistic reply using an LLM.

## Features
- **Single endpoint** `/process` — returns `{ transcript, answer }`.
- **API key authentication** via `X-API-Key` header.
- **Configurable** via `.env`.
- **Async** requests to external APIs (non-blocking).

## Requirements
- Python 3.12+
- Poetry
- Hugging Face account + API token.

## Installation

```bash
# Clone the repo
git clone https://github.com/sashcheka/audio-llm-api.git
cd audio-llm-api.git

# Install dependencies
poetry install
````

## Configuration

Create a `.env` file in the project root:

```env
HF_TOKEN=<your_huggingface_token>
API_KEY=<your_api_key_for_requests>
ASR_MODEL=openai/whisper-large-v3
LLM_MODEL=mistralai/Mistral-7B-Instruct-v0.2:featherless-ai
```

## Running locally

```bash
# Start the FastAPI server
poetry run uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

### Example request

#### Windows PowerShell
```powershell
curl.exe -X POST "http://127.0.0.1:8000/process" `
  -H "X-API-Key: <your_api_key_here>" `
  -F "file=@</path/to/audio.mp3>"
```

#### Linux

```bash
curl -X POST "http://127.0.0.1:8000/process" \
  -H "X-API-Key: <your_api_key_here>" \
  -F "file=@</path/to/audio.mp3>"
```

#### macOS

```bash
curl -X POST "http://127.0.0.1:8000/process" \
  -H "X-API-Key: <your_api_key_here>" \
  -F "file=@</path/to/audio.mp3>"
```

### Response:

```json
{
  "transcript": "Hello world",
  "answer": "It sounds like a friendly greeting."
}
```
