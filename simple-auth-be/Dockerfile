FROM python:3.12-slim

WORKDIR /app

# Install system dependencies 
RUN apt-get update && apt-get install -y --no-install-recommends \
	gcc \
	libpq-dev \
	curl \
	&& rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:${PATH}"

# Copy dependencies
COPY pyproject.toml .

# Install dependencies via uv 
RUN uv sync --dev

# No COPY for dev purposes use volume mount
# Start Uvicorn serice on 0.0.0.0:8080 for host
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
