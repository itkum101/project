
# Use Python 3.10 Slim as the base image
FROM python:3.10-slim AS builder

# Set the working directory
WORKDIR /app

# Install system dependencies required for Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libc-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage caching
COPY requirements.txt .

# Install dependencies efficiently
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt

# Use a smaller runtime image
FROM python:3.10-slim

WORKDIR /app

# Copy only the necessary files from builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application files
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Use Gunicorn instead of Flask’s built-in server (better for production)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
