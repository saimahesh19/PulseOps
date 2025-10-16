# PulseOps

**AIALERT** is a fully containerized DevOps and Observability Proof-of-Concept (POC) project. It demonstrates a scalable, event-driven architecture with monitoring, logging, and auto-scaling capabilities. **No AI/ML is used** — the “ML service” here is a placeholder for any microservice that processes tasks from a queue.  

---

## 🚀 Features

- Event-driven microservices using **RabbitMQ** and **Redis**.
- Containerized services using **Docker** and optionally deployable to **Kubernetes (Minikube)**.
- Observability stack:
  - **Metrics:** Telegraf → VictoriaMetrics
  - **Logs:** Promtail → Loki → Grafana
- Auto-scaling with **KEDA** based on RabbitMQ queue length.
- Local and persistent storage for logs and metrics.
- Fully configurable via YAML and environment variables.

---

## 🎗️ Project Architecture

```
        +------------+        +-------------+
        |  Producer  | -----> |  RabbitMQ   |
        +------------+        +-------------+
                                   |
                                   v
                            +--------------+
                            |  ML Service  |
                            +--------------+
                                   |
             ----------------------+---------------------
            |                                            |
     +--------------+                             +---------------+
     |  Telegraf    |                             |   Promtail    |
     | (metrics)    |                             | (logs)        |
     +--------------+                             +---------------+
            |                                            |
            v                                            v
  +-------------------+                         +---------------+
  | VictoriaMetrics   |                         |    Loki       |
  +-------------------+                         +---------------+
                                                    |
                                                    v
                                               +----------+
                                               | Grafana  |
                                               +----------+
```

**Key Highlights:**

- **KEDA:** Automatically scales the ML service based on the RabbitMQ queue length.
- **Grafana:** Provides a unified dashboard for both metrics and logs.
- **Persistent storage:** `loki_data/` and VictoriaMetrics volumes ensure logs/metrics survive container restarts.

---

## 🛠️ Tech Stack

| Layer                 | Technology / Tool         |
|-----------------------|--------------------------|
| Messaging Queue       | RabbitMQ                 |
| Cache / Storage       | Redis                    |
| Metrics               | Telegraf, VictoriaMetrics|
| Logging               | Promtail, Loki           |
| Dashboard             | Grafana                  |
| Orchestration         | Docker, Docker Compose   |
| Auto-scaling          | KEDA                     |
| Microservices         | Python (Producer & ML)   |

---

## 📁 Project Structure

```
PulseOps/
├── KEYS/                  # Optional secrets or certificates
├── docker-compose.yml      # Docker Compose orchestration
├── get-docker.sh           # Script to install Docker
├── k8s/                    # Kubernetes manifests & configs
├── loki_data/              # Persistent storage for Loki
├── ml_service/             # ML Service microservice
├── producer/               # Producer microservice
└── requirements.txt        # Python dependencies
```

---

## ⚙️ Setup Instructions

### **1. Clone the repository**

```bash
git clone https://github.com/your-username/AIALERT.git
cd AIALERT
```

### **2. Start using Docker Compose**

```bash
docker compose up -d
```

This will start all services:

- RabbitMQ → `http://localhost:15672` (guest/guest)
- Redis → `localhost:6379`
- VictoriaMetrics → `http://localhost:8428/metrics`
- Loki → `http://localhost:3100`
- Promtail → log shipping to Loki
- Grafana → `http://localhost:3000` (admin/admin)

### **3. (Optional) Kubernetes Deployment**

If you want to deploy on **Minikube/Kubernetes**:

```bash
kubectl apply -f k8s/
```

- Use `mlservice-scaledobject.yaml` to enable **KEDA auto-scaling**.

### **4. Verify Observability**

- Grafana dashboards:
  - Metrics: VictoriaMetrics as data source
  - Logs: Loki as data source
- Telegraf and Promtail must be running to push data to respective stores.

---

## ⚡ Notes

- Ensure **Docker is installed** (`get-docker.sh` helps for Linux).
- Persistent directories (`loki_data/` and VictoriaMetrics volume) must be writable.
- Adjust config files in `k8s/` or `telegraf/` as per your environment.
- ML service can be replaced with any consumer microservice that reads from RabbitMQ.

---

## 📈 Screenshots / Dashboards
-Keda Auto Scaling

![WhatsApp Image 2025-10-16 at 15 45 21_20ebbbe4](https://github.com/user-attachments/assets/8a0b4713-f111-4297-bece-ed8af97d210f)

- Grafana metrics dashboards

 <img width="1365" height="559" alt="image" src="https://github.com/user-attachments/assets/5c439571-a82a-48a9-807d-e9ff678ef81e" />

- Logs aggregated in Loki

<img width="778" height="584" alt="image" src="https://github.com/user-attachments/assets/7513cc01-105e-4073-b2d6-9c1128bdd298" />

---

## 🔧 License

This project is **MIT Licensed** — free to use and modify.

---

## 👤 Author

**Sai Mahesh Marpu**  
[LinkedIn Portfolio](https://saimaheshmarpuportifolio.mgx.world)

