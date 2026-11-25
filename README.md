# Qwen on Ollama: Local LLM Test

A minimal script that calls a **locally running LLM** (Alibaba's `qwen:0.5b`, served by [Ollama](https://ollama.com)) through Ollama's REST API. No API key, no cloud, no cost.

## What it does
It sends one prompt (*"Explain JWT authentication in simple terms"*) to `http://localhost:11434/api/generate` and prints the model's answer.

## Run
```bash
# 1. Install Ollama (https://ollama.com/download), then pull the model
ollama pull qwen:0.5b
ollama serve            # skip this if the Ollama app is already running

# 2. Run the script
pip install -r requirements.txt
python app.py
```

Try other models by changing `"model"` in `app.py` (for example `llama3.2`, `qwen2.5:1.5b`), and change `"prompt"` to ask something else.

## Tech stack
Python · requests · Ollama · Qwen
