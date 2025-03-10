FROM python:3.12-slim AS base
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
COPY README.md README.md
RUN uv sync

FROM base AS runner
COPY . .
EXPOSE 8000
CMD ["uv", "run", "src/manage.py", "runserver", "0.0.0.0:8000"]