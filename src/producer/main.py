import json
import os
import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kafka import KafkaProducer
from kafka.errors import KafkaError

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración del entorno
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
TOPIC_NAME = os.getenv("KAFKA_TOPIC", "test-topic")

logger.info(f"🚀 Kafka broker: {KAFKA_BROKER}")
logger.info(f"📦 Kafka topic: {TOPIC_NAME}")

# Inicializar FastAPI
app = FastAPI()

# Inicializar Kafka producer
try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        retries=5
    )
    logger.info("✅ KafkaProducer inicializado correctamente.")
except KafkaError as e:
    logger.error(f"❌ Error al conectar con Kafka: {e}")
    raise

# Modelo de mensaje
class Message(BaseModel):
    msg: str

# Endpoint para enviar mensajes
@app.post("/send")
async def send_message(message: Message):
    try:
        logger.info(f"📤 Enviando mensaje: {message.msg}")
        future = producer.send(TOPIC_NAME, {"message": message.msg})
        result = future.get(timeout=10)
        logger.info(f"✅ Mensaje enviado a Kafka: {result}")
        return {"status": "Message sent", "topic": TOPIC_NAME}
    except KafkaError as e:
        logger.error(f"❌ Error enviando mensaje a Kafka: {e}")
        raise HTTPException(status_code=500, detail="Error sending message to Kafka")
