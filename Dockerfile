# Dockerfile for Flask server
FROM python:3.12.2

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /start_ollama.sh

CMD ["python", "open_rag_api/app.py"]



