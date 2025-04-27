# 🚀 Docker Experiment 1: Streamlit Spiral Visualization App

Welcome to the **Streamlit Spiral Visualization App**!  
This project showcases a simple, interactive Python app built with **Streamlit**, allowing you to customize and visualize a spiral in real-time. It's fully **Dockerized** for seamless deployment and consistency across environments.

---

## 🌟 Features

- **Interactive Controls**: Adjust the number of points and turns using sliders.
- **Live Updates**: See the spiral update instantly as you tweak the settings.
- **Dockerized Setup**: The app runs inside a Docker container, ensuring portability and eliminating "it works on my machine" issues.

---

## 🚀 Technologies Used

- **Python 3** – Core programming language.
- **Streamlit** – For building the interactive web interface.
- **Altair** – For rendering beautiful visualizations.
- **Pandas** – For managing data structures.
- **Docker** – For containerizing and deploying the app easily.

---

## ⚙️ Prerequisites

Before you start, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

## 🛠 Getting Started

Follow these steps to clone, build, and run the application:

### Step 1: Clone the Repository

```bash
git clone https://github.com/BhavyaDhimxn/container-experiments.git
cd container-experiments
```

### Step 2: Add Dependencies

Create a `requirements.txt` file (if not already present) with:

```
streamlit
altair
pandas
```

### Step 3: Build the Docker Image

From the project directory, build the Docker image:

```bash
docker build -t streamlit .
```

After building, verify your image:

- **Docker Desktop**: Check the **Images** tab.
- **Command Line**: Run:

```bash
docker images
```

### Step 4: Run the Docker Container

Start the application by running:

```bash
docker run -p 8501:8501 streamlit
```

This maps port `8501` inside the container to your local machine.

### Step 5: Open the App

Visit:

```
http://localhost:8501
```

You'll now see the interactive Spiral Visualization App!

---

## 🌀 App Overview

**Sliders**:

- **Number of Points**: Defines how many points build the spiral.
- **Number of Turns**: Controls how many full rotations the spiral completes.

**Real-Time Visualization**:

The spiral regenerates dynamically with every adjustment.

**Under the Hood**:

- The spiral points are computed using **polar coordinates**.
- `namedtuple` structures the point data.
- **Altair** renders the points in a clean scatter plot inside the Streamlit app.

---

## 💻 Code Overview

```python
# Imports
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from collections import namedtuple

# Define Point structure
Point = namedtuple('Point', ['x', 'y'])

# Generate spiral data
def generate_spiral(num_points, num_turns):
    data = []
    for i in range(num_points):
        angle = 2 * np.pi * num_turns * (i / num_points)
        radius = i / num_points
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        data.append(Point(x, y))
    return data

# Streamlit app
st.title("Interactive Spiral Visualization")
num_points = st.slider('Number of Points in Spiral', 50, 1000, 500)
num_turns = st.slider('Number of Turns in Spiral', 1, 10, 5)
spiral_data = generate_spiral(num_points, num_turns)
spiral_df = pd.DataFrame(spiral_data, columns=['x', 'y'])

chart = alt.Chart(spiral_df).mark_circle(size=3).encode(x='x', y='y').properties(width=600, height=600)
st.altair_chart(chart, use_container_width=True)
```

---

## 📦 Dockerfile

```dockerfile
# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py"]
```

---

## 🛠 Troubleshooting

- **Check container logs** if the app isn't starting:

```bash
docker logs <container_id>
```

- **Verify dependencies**: Ensure `requirements.txt` includes all necessary packages and they are installed correctly.

---

