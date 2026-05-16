# ----------------------------------------------------------------------------
# Customer Accounts Microservice - Production Docker Image
# Multi-stage build for a small, secure runtime image
# ----------------------------------------------------------------------------

FROM python:3.9-slim AS base

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install OS-level build dependencies (needed for psycopg2)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create application directory
WORKDIR /app

# Install Python dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --upgrade pip wheel \
    && pip install -r requirements.txt

# Copy the application source
COPY service/ ./service/
COPY wsgi.py .

# Create a non-root user and switch to it for security
RUN useradd --uid 1001 --create-home --shell /bin/bash flask \
    && chown -R flask:flask /app
USER flask

# Expose the application port
EXPOSE 8080

# Health check used by Docker and Kubernetes probes
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health').read()" || exit 1

# Run the service with gunicorn in production
CMD ["gunicorn", "--bind=0.0.0.0:8080", "--workers=2", "--log-level=info", "wsgi:app"]
