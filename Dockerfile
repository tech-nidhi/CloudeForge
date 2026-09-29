# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Ensure Python outputs logs directly to stdout/stderr without buffering
ENV PYTHONUNBUFFERED=1

# Copy dependency definition first for optimal Docker layer caching
COPY requirements.txt .

# Install dependencies without caching wheels to keep image minimal
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port (matching Flask 0.0.0.0:5000)
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
