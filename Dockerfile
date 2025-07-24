FROM python:3.10-slim

WORKDIR /app

COPY jubin.py .

CMD ["python", "jubin.py"]