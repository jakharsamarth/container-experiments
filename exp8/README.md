# 🚀 Docker Experiment 8: Deploying a Dockerized Application on AWS EC2

This guide demonstrates how to deploy a **Dockerized application** on an **AWS EC2 instance**. You'll set up Docker, transfer application files, build a Docker image, and run the application — all on the cloud!

---

## 📋 Prerequisites

✔️ AWS EC2 Instance (Amazon Linux 2)  
✔️ SSH Key Pair (`vs-kp-1.pem`)  
✔️ Docker installed on EC2  
✔️ Required files: `Dockerfile`, `app.py`, `requirements.txt`, `mushrooms.csv`

---

## 🛠️ Setup and Deployment Steps

### 🔹 Step 1: Update the System

```bash
sudo yum update -y
```

---

### 🔹 Step 2: Install Docker

```bash
sudo amazon-linux-extras install docker
```

---

### 🔹 Step 3: Start the Docker Service

```bash
sudo service docker start
```

---

### 🔹 Step 4: Create a Directory for Application Files

```bash
mkdir downloads
```

---

### 🔹 Step 5: Transfer Files to EC2

```bash
chmod 600 vs-kp-1.pem
scp -i vs-kp-1.pem Dockerfile app.py requirements.txt mushrooms.csv ec2-user@<EC2-Public-IP>:/home/ec2-user/downloads
```

---

### 🔹 Step 6: Build the Docker Image

```bash
cd downloads
sudo docker build -t my_app:v1.0 -f Dockerfile .
```

---

### 🔹 Step 7: Run the Application Container

```bash
sudo docker run -d -p 8501:8501 my_app:v1.0
```

---

## 🌍 Access the Application

✅ Open your browser and navigate to:

```
http://<EC2-Public-IP>:8501
```

---

## 🔍 Managing the Container

- **Check running containers:**

```bash
sudo docker ps
```

- **View container logs:**

```bash
sudo docker logs <container-id>
```

- **Stop the container:**

```bash
sudo docker stop <container-id>
```

---


## 📢 Important Notes

- Ensure the **EC2 security group** allows **inbound traffic** on **port 8501**.
- To restart Docker if needed:

```bash
sudo service docker restart
```

- If the container stops unexpectedly, check logs for troubleshooting.

---

### 🎯 Summary

✅ Updated EC2 instance and installed Docker  
✅ Transferred application files securely  
✅ Built and ran the Dockerized app on AWS EC2  
✅ Accessed the live app from anywhere 🚀

---

