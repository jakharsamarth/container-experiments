# 🚀 Docker Experiment 3: 🐍 Python Logging App with Docker

This project showcases building a simple Python app that continuously writes logs to a file, running inside a Docker container. Logs are persisted using a Docker volume, surviving container restarts or removal.

---

## 📂 Project Structure

```plaintext
.
├── app.py          # Python script that generates logs
└── Dockerfile      # Dockerfile to build the Docker image
```

---

## 📥 Prerequisites

Make sure Docker is installed on your machine:

[Install Docker](https://docs.docker.com/get-docker/)

---

## 🛠 Steps to Build and Run

### ✍️ Step 1: Create the Python Logging App

Create `app.py` with the following code:

```python
import time
import os

LOG_FILE = "/data/app.log"
MAX_LOG_SIZE = 1 * 1024 * 1024  # 1MB

def rotate_logs():
    """Rotate the log file if it exceeds the max size."""
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) >= MAX_LOG_SIZE:
        os.rename(LOG_FILE, "/data/app.log.bak")

def log_message():
    """Log a message with a timestamp."""
    message = f"[{time.ctime()}] - App is running\n"
    print(message, end="")

    with open(LOG_FILE, "a") as f:
        f.write(message)
        f.flush()

if __name__ == "__main__":
    while True:
        rotate_logs()
        log_message()
        time.sleep(5)
```

### 🔧 Improvements:
- Log rotation to prevent unlimited file growth.
- Logs both to file and console with timestamps.

---

### 🛠 Step 2: Write the Dockerfile

Create a `Dockerfile` with the following content:

```dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application code
COPY app.py /app/app.py

# Create directory for logs
RUN mkdir -p /data

# Run the app
CMD ["python", "app.py"]
```

### 🔧 Highlights:
- Uses **Python 3.9-slim** for a smaller image size.
- Ensures `/data` directory exists for log storage.

---

### 🚀 Step 3: Build the Docker Image

Build the image by running:

```bash
docker build -t python-log-app .
```

This will create a Docker image named `python-log-app`.

---

### 🚀 Step 4: Run the Container with a Volume

Start the container with a volume for persistent storage:

```bash
docker run -d --name log-container -v my-app-data:/data python-log-app
```

#### Options Explained:
- `-d`: Detached mode.
- `--name log-container`: Names the container.
- `-v my-app-data:/data`: Mounts the volume `my-app-data` to `/data`.

---

## 🧐 Step 5: Checking Logs

### 🔍 1. Verify the container is running:
```bash
docker ps
```

### 🔍 2. View live container logs:
```bash
docker logs -f log-container
```

### 🔍 3. Inspect log file inside the container:
```bash
docker exec -it log-container sh
cd /data
cat app.log
```

### 🔍 4. Check volume details:
```bash
docker volume inspect my-app-data
```

---

## 🧹 Stopping and Cleaning Up

### 🛑 1. Stop the container:
```bash
docker stop log-container
```

### 🗑 2. Remove the container:
```bash
docker rm log-container
```

### 🗑 3. Remove the image (optional):
```bash
docker rmi python-log-app
```

### 🗑 4. Remove the volume (optional):
```bash
docker volume rm my-app-data
```

---

## ⚠️ Important Notes

- Logs are safely stored inside the Docker volume `my-app-data`.
- Log rotation avoids oversized log files.
- Sleep interval and log formats are customizable.

