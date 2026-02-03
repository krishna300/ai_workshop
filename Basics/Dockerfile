# ---------------------------
# Dockerfile for Basics project
# ---------------------------

# Use official Python slim image
FROM python:3.13-slim

# ---------------------------
# Install system dependencies for Graphviz and compilation
# ---------------------------
RUN apt-get update && apt-get install -y \
    graphviz \
    build-essential \
    libgraphviz-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------
# Set environment variables for PyGraphviz
# ---------------------------
ENV GRAPHVIZ_INCLUDE=/usr/include/graphviz
ENV GRAPHVIZ_LIB=/usr/lib/graphviz

# ---------------------------
# Set working directory
# ---------------------------
WORKDIR /app

# ---------------------------
# Copy project files
# ---------------------------
COPY . /app

# ---------------------------
# Install Python dependencies
# ---------------------------
# Upgrade pip first
RUN pip install --upgrade pip

# Install from requirements.txt if it exists
# Make sure requirements.txt includes at least:
# uv, langgraph, pygraphviz
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# ---------------------------
# Default command when container runs
# ---------------------------
CMD ["uv", "run", "python", "dev.py"]
