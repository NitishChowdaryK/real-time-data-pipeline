from kafka import KafkaProducer
import json, time, random
producer = KafkaProducer(bootstrap_servers='host.docker.internal:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


for i in range(1000):
    record = {
        'transaction_id': f"TX{i}",
        'timestamp': time.time(),
        'security': random.choice(['stocks', 'bonds', 'etfs']),
        'region': random.choice(['US', 'EU', 'ASIA']),
        'value': round(random.uniform(100, 10000), 2)
    }
    producer.send('financial-logs', record)
    time.sleep(0.05)

print("Produced 1000 messages.")
