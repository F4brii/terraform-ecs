# consumer.py
import os
import json
import time
import logging
from kafka import KafkaConsumer
from kafka.errors import KafkaError, NoBrokersAvailable

# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Configuración desde variables de entorno
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
TOPIC_NAME = os.getenv("KAFKA_TOPIC", "test-topic")
GROUP_ID = "consumer-group"

def start_consumer():
    while True:
        try:
            logger.info(f"🔌 Connecting to Kafka broker: {KAFKA_BROKER}")
            consumer = KafkaConsumer(
                TOPIC_NAME,
                bootstrap_servers=KAFKA_BROKER,
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                group_id=GROUP_ID,
                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                consumer_timeout_ms=None
            )
            logger.info("🚀 Consumer is ready and listening for messages...")

            for message in consumer:
                logger.info(f"📩 Received: {message.value}")

        except NoBrokersAvailable:
            logger.error("❌ No brokers available. Retrying in 5 seconds...")
        except KafkaError as e:
            logger.error(f"❌ Kafka error: {e}")
        except Exception as e:
            logger.exception(f"❌ Unexpected error: {e}")

        logger.info("🔁 Restarting Kafka consumer in 5 seconds...")
        time.sleep(5)

if __name__ == "__main__":
    start_consumer()
