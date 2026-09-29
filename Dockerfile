# FIX: Using a secure slim base image instead of a massive one
FROM python:3.11-slim

# Create a non-root user and group for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Install dependencies first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary application source code
COPY app/ .

# FIX: Change ownership of the app directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user (Prevents running as root)
USER appuser

# Expose a non- port (e.g., 5000 instead of 80)
EXPOSE 5000

# FIX: Using JSON array format for CMD to prevent shell injection and handle OS signals properly
CMD ["python", "app.py"]