# 🚀 Real-Time Data Pipeline: Kafka → Spark → Snowflake

This project implements a **real-time streaming data pipeline** using:
- **Apache Kafka** for ingesting data
- **Apache Spark Structured Streaming** for processing
- **Snowflake** as the data warehouse
- **Prometheus** for monitoring


---

## 📦 Architecture Overview

```text
Kafka Producer --> Kafka Broker --> Spark Streaming --> Snowflake
                                   |
                           Prometheus (Monitoring)


🛠️ Tech Stack
Component	Tech Used
Stream Source	Apache Kafka
Processing	Apache Spark Structured Streaming
Data Sink	Snowflake
Monitoring	Prometheus
Orchestration	Docker + docker-compose
Dashboard UI	React (planned extension)


spark-pipeline-project/
│
├── docker/                   # Docker setup for Kafka, Prometheus, Grafana
├── kafka_producer/          # Kafka Python producer script
├── spark_app/               # Spark job to read from Kafka and write to Snowflake
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Combined services
├── prometheus.yml           # Prometheus config
└── README.md                # This file


⚙️ Setup Instructions
🔹 1. Clone the Repository
git clone https://github.com/NitishchowdaryK/real-time-data-pipeline.git
cd real-time-data-pipeline
🔹 2. Start Docker Services
cd docker
docker-compose up -d
Brings up:
Kafka & Zookeeper
Prometheus on localhost:9091
🔹 3. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
🔹 4. Produce Kafka Data
python kafka_producer/producer.py
🔹 5. Run Spark Job to Push to Snowflake
spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2,net.snowflake:spark-snowflake_2.12:2.11.0-spark_3.3 \
  spark_app/spark_to_snowflake.py
❄️ Snowflake Table Schema
CREATE TABLE TRANSACTIONS_TABLE (
  transaction_id STRING,
  timestamp FLOAT,
  security STRING,
  region STRING,
  value FLOAT
);
📊 Monitoring Dashboard
Prometheus: http://localhost:9091
🔐 Environment Variables
SNOWFLAKE_USER=Nitishchowdary22
SNOWFLAKE_PASSWORD=Nitishchowdary@2002
SNOWFLAKE_ACCOUNT=Nitish Chowdary Kolupoti
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=FINANCE_DB
SNOWFLAKE_SCHEMA=TRANSACTIONS

🧠 Author
Nitish Chowdary


