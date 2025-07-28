FROM python:3.10-slim

WORKDIR /app

COPY jubin.py .

RUN pip install flask

CMD ["python", "jubin.py"]