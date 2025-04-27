# 🚀 Docker Experiment 9: Minikube with Docker on Windows ☸️

Run **Kubernetes locally** using **Minikube** and **Docker** — a simple, fast, and effective way to practice Kubernetes without a full cloud setup!

---

## 🌟 Introduction

**Minikube** is a lightweight tool that spins up a single-node Kubernetes cluster locally.  
It’s perfect for developers wanting to **experiment**, **test**, and **learn Kubernetes** — right from their machine!

---

## 🛠️ Prerequisites

Before starting, ensure the following are installed:

### ✅ 1. Install Docker Desktop 🐳

- Download from [Docker Desktop](https://www.docker.com/products/docker-desktop).
- Enable **WSL 2 Backend** (recommended).
- If using **Windows Pro/Enterprise**, enable **Hyper-V** support.

---

### ✅ 2. Install Minikube 📦

Install via **Chocolatey** (run CMD/PowerShell as Admin):

```bash
choco install minikube
```

If Chocolatey isn't available, [follow manual installation](https://minikube.sigs.k8s.io/docs/start/).

---

### ✅ 3. Install kubectl (Kubernetes CLI) 🔗

```bash
choco install kubernetes-cli
```

Verify installation:

```bash
kubectl version --client
```

---

## 🚀 Setting Up Minikube with Docker

### ✅ Step 1: Start Minikube 🏁

Ensure Docker is running, then start Minikube using Docker as the driver:

```bash
minikube start --driver=docker
```

Check the cluster status:

```bash
minikube status
```

---

## 🏗️ Deploying an Application in Minikube

### ✅ Step 2: Deploy Nginx Web Server 🌐

#### 1️⃣ Create an Nginx Deployment

```bash
kubectl create deployment nginx --image=nginx
```

---

#### 2️⃣ Expose the Deployment

```bash
kubectl expose deployment nginx --type=NodePort --port=80
```

---

#### 3️⃣ Access the Service

Get the service URL:

```bash
minikube service nginx --url
```

✅ Open the provided URL in your browser — you should see the **Nginx welcome page**! 🎉

---

## ⚙️ Managing the Kubernetes Cluster

### 🔹 Check Running Pods

```bash
kubectl get pods
```

---

### 🔹 Scale the Deployment

Increase replicas to 3:

```bash
kubectl scale deployment nginx --replicas=3
```

Confirm the updated pods:

```bash
kubectl get pods
```

---

### 🔹 Delete Deployment and Service

```bash
kubectl delete service nginx
kubectl delete deployment nginx
```

---

## ❌ Stopping and Cleaning Up Minikube

### ✅ Stop Minikube

```bash
minikube stop
```

---

### ✅ Delete the Cluster

```bash
minikube delete
```

_This removes all Kubernetes resources and resets the environment._

---

## 🎯 Conclusion

By running **Minikube with Docker**, you unlock a powerful local Kubernetes environment for:

✅ Testing deployments  
✅ Exploring Kubernetes resources  
✅ Practicing scaling, networking, and app management  

---

