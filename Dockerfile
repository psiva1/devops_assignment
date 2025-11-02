FROM python:3.10-slim

RUN mkdir -p /app

WORKDIR /app

COPY main.py /app

RUN pip install flask prometheus_client

EXPOSE 8000

CMD ["python", "main.py"]
