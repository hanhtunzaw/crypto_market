# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run the full pipeline
CMD ["python", "pipeline_scheduler.py"]