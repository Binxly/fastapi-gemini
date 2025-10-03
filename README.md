# Simple FastAPI + Gemini Setup

Start the Server:

```bash
uvicorn src.main:app --reload
```

### Example payloads

Unauthenticated:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "This is a test message. Write a story."
}'
```
Use [JWT.io](https://www.jwt.io/) to test auth.

Auth Token:
```bash
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ******" \
-d '{"prompt": "Why is the sky blue?"}'
```

 replace ****** with your generated web token
