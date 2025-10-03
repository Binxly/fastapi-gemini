# Simple FastAPI + Gemini Setup

Start the Server:

```bash
uvicorn src.main:app --reload
```

Example payload:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "This is a test message. Write a story."
}'
```
