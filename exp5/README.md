# 🚀 Docker Experiment 5: 🐬 MySQL Container with Docker

This project sets up a **MySQL Docker container** with automatic database initialization. It's a quick and simple way to get a MySQL server up and running inside a container.

---

## 📥 Features

✅ **Pre-configured MySQL database** on container startup  
✅ **Automatic execution of `database.sql`** during first run  
✅ **Quick setup** with simple Docker commands  

---

## 🛠️ Setup Instructions

### 📂 Step 1: Clone the Repository

```bash
git clone https://github.com/jakharsamarth/container-experiments.git
cd container-experiments
```

---

### 🐳 Step 2: Build the Docker Image

Build the custom MySQL Docker image:

```bash
docker build -t mysql-container .
```

---

### 🚀 Step 3: Run the MySQL Container

Start a new MySQL container:

```bash
docker run --name mysql-container -d mysql-container
```

---

### 🛢️ Step 4: Connect to the MySQL Server

Access the MySQL shell inside the running container:

```bash
docker exec -it mysql-container mysql -u root -p
```

➡️ When prompted, enter the password: **root**

---

### 🧹 Step 5: Stop and Remove the Container

#### To Stop the Container:

```bash
docker stop mysql-container
```

#### To Remove the Container:

```bash
docker rm mysql-container
```

---

## 📁 Project Structure

```plaintext
Docker_Practices/
│── database.sql  # SQL script for initial database setup
│── Dockerfile    # Dockerfile to configure the MySQL container
│── README.md     # Project documentation
```

---

## 📌 Notes

- The `database.sql` script runs **only once** during the initial container startup.
- The default **root password** is set to `root`.  
  ➡️ **Important**: Change it in production for security best practices!

---

## 🔗 Repository

🔗 **GitHub**: [jakharsamarth/container-experiments](https://github.com/jakharsamarth/container-experiments.git)

---

## 📜 License

This project is **open-source** and free to use.  
Contributions are welcome! 🚀

---
