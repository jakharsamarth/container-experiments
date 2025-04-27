# 🚀 Docker Experiment 4: 🖥️ Streamlit App with PostgreSQL Using Docker

This project walks you through setting up a Streamlit app that connects to a PostgreSQL database inside Docker containers. It includes creating a custom Docker network, launching a PostgreSQL container, inserting sample data, and deploying a Streamlit app to fetch and display the data.

---

## 📥 Prerequisites

- Docker installed
- Basic knowledge of Docker, PostgreSQL, and Python

---

## 🛠️ Setup Instructions

### 🌐 Step 1: Create a Custom Docker Network

```bash
docker network create --driver bridge my_custom_network
```
This allows the PostgreSQL and Streamlit containers to communicate.

---

### 🛢️ Step 2: Launch PostgreSQL Container

```bash
docker run -d \
  --name my_postgres \
  --network my_custom_network \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=adminpassword \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  postgres
```

✅ Sets up PostgreSQL with:
- **User**: `admin`
- **Password**: `adminpassword`
- **Database**: `mydb`
- **Port**: `5432`

---

### ✍️ Step 3: Insert Dummy Data

#### Connect to PostgreSQL

```bash
docker exec -it my_postgres psql -U admin -d mydb
```

#### Create Table and Insert Users

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

INSERT INTO users (name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Charlie Brown', 'charlie@example.com');

SELECT * FROM users;
```

#### Exit the PostgreSQL CLI
```plaintext
\q
```

---

### 🖥️ Step 4: Create the Streamlit Application

Create a file called `stream.py` with the following content:

```python
import streamlit as st
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="mydb",
        user="admin",
        password="adminpassword",
        host="my_postgres",
        port="5432"
    )
    return conn

st.title("Streamlit App with PostgreSQL")

try:
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()

    st.write("### User Data from PostgreSQL")
    for row in rows:
        st.write(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    
    cur.close()
    conn.close()
except Exception as e:
    st.error(f"Error connecting to database: {e}")
```

---

### 🐳 Step 5: Write the Dockerfile for Streamlit

Create a `Dockerfile`:

```dockerfile
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir streamlit psycopg2

EXPOSE 8501

CMD ["streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

### 🚀 Step 6: Build and Run the Streamlit Container

#### Build the Image

```bash
docker build -t my_streamlit_app .
```

#### Run the Streamlit Container

```bash
docker run -d \
  --name streamlit_app \
  --network my_custom_network \
  -p 8501:8501 \
  my_streamlit_app
```

---

### 🧪 Step 7: Test Everything

- Open your browser and navigate to: [http://localhost:8501](http://localhost:8501)
- You should see the list of users retrieved from PostgreSQL!

---

## 📝 Summary

✅ Created a custom Docker network (`my_custom_network`)  
✅ Launched a PostgreSQL container and inserted dummy users  
✅ Built a Streamlit app that connects to PostgreSQL  
✅ Deployed the app in a Docker container  
✅ Accessed the app via `http://localhost:8501`

---

## 🧹 Cleanup

To stop and remove everything:

```bash
docker stop my_postgres streamlit_app
docker rm my_postgres streamlit_app
docker network rm my_custom_network
```

---

