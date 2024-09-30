# Use python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies and required packages
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    libx11-6 \
    libx11-dev \
    libglib2.0-0 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Add Azure credentials
COPY azure_credentials.txt /app/azure_credentials.txt

# Set the DISPLAY environment variable for X11 forwarding
ENV DISPLAY=:0

# Set the credentials file path as an environment variable
ENV AZURE_CREDENTIALS_FILE=/app/azure_credentials.txt

# Run the application
CMD ["python", "Azure-BlobStorage-Manager.py"]
