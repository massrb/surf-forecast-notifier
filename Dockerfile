# Use an official Python slim image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies needed for Playwright
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    unzip \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    libgbm-dev \
    libgtk-3-0 \
    libxshmfence-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps

# Copy source code
COPY . .

COPY urls.txt .
COPY requirements.txt .

# Expose port for Cloud Run
EXPOSE 8080

# Start the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.main:app"]
