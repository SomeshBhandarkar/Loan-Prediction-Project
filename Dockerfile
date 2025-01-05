# Dockerfile-streamlit
FROM python:3.9

WORKDIR /app

# Install system dependencies
# RUN apt-get update && apt-get install -y ffmpeg

# Copy Streamlit code
COPY app/streamlit /app/streamlit

# Copy the requirements.txt file from the root directory
COPY requirements.txt /app/requirements.txt

# Install required Python packages
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8501

# Start Streamlit
CMD ["streamlit", "run", "streamlit/app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]