
# Use Python 3.10 Slim as the base image
FROM python:3.10-slim AS builder

# Set the working directory
WORKDIR /app

# Copy only requirements first to leverage caching
COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

# Copy the application files
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Use Gunicorn instead of Flask’s built-in server (better for production)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
