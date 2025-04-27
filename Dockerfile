# Use official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "stream.py"]
