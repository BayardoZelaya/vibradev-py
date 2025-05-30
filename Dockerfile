#create docker file for fastapi
FROM python:3.13.3-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev && \
    pip install --upgrade pip && \
    pip install uv && \
    pip install "fastapi[standard]" && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .

RUN uv venv && \
    . .venv/bin/activate && \
    uv pip install -e .

COPY . .

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

RUN mkdir -p app/logs

CMD ["fastapi", "run", "app/api/v1/api.py", "--port", "8080"]   