import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen:0.5b",
        "prompt": "Explain JWT authentication in simple terms",
        "stream": False
    }
)

print(response.json()["response"])