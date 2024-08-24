# Use a Python base image
FROM python:3.11-slim

# Install PostgreSQL client and development headers
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && apt-get clean

# Set the working directory
WORKDIR /workspaces/${localWorkspaceFolderBasename}

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose necessary ports
EXPOSE 5000
EXPOSE 5432
