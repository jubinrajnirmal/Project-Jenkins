FROM python:3.9-slim

WORKDIR /app

COPY jubin.py .

CMD ["python", "jubin.py"]