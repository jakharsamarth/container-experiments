# 🚀 Docker Experiment 6: 🛜 Docker Network Setup and Testing

This project demonstrates how to create and use a **custom Docker network** (`net-bridge`) for seamless **inter-container communication**. It highlights how containers interact within a user-defined bridge network.

---

## 📋 Experiment Overview

In this experiment, you'll:

✅ Create a **custom bridge network**  
✅ Run **multiple containers** inside the network  
✅ **Inspect** network configurations  
✅ **Test** communication between containers using IP and container names  

---

## 🛠️ Setup Instructions

### 🌐 Step 1: Create a Custom Docker Network

Create a new bridge network with a specified subnet and IP range:

```bash
docker network create --driver bridge --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 net-bridge
```

---

### 📦 Step 2: Run Containers and Attach to the Network

#### 🗄️ Launch the Database Container

```bash
docker run -itd --net=net-bridge --name=cont_database redis
```

#### 🖥️ Launch the Server Container

```bash
docker run -dit --name server-A --network net-bridge busybox
```

---

### 🔍 Step 3: Inspect Network and Containers

#### 🔧 Inspect the Network

```bash
docker network inspect net-bridge
```

#### 🔧 Inspect a Container

```bash
docker inspect cont_database
```

#### 🌐 Get Container IP Address

```bash
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' cont_database
```

---

### 🔗 Step 4: Test Connectivity

#### 🖥 Access the Server Container Shell

```bash
docker exec -it server-A sh
```

#### 📡 Ping Database Container by IP Address

```bash
ping 172.20.240.1  # Replace with actual IP address
```

#### 📡 Ping Database Container by Name

```bash
ping cont_database
```

---

## 📌 Observations

✅ Containers communicate directly within the custom bridge network.  
✅ IP-based communication works seamlessly.  
✅ Container name resolution might **not always work** in lightweight images like BusyBox.  
✅ `docker inspect` is very useful for retrieving IP addresses and network details.

---

## 🏁 Conclusion

This experiment demonstrates Docker's **networking capabilities**, particularly how to configure and test **custom bridge networks**.  
Mastering Docker networking is essential for building **scalable, secure, and efficient** container-based systems and microservices.

---

✅ Successful inter-container communication achieved! 🚀
