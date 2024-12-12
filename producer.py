from kafka import KafkaProducer
from faker import Faker
import json
import time

# Configuração do Producer
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Gerador de dados fictícios
fake = Faker()

# Nome do tópico
topic = 'meu_topico'

while True:
    # Gera um dado fictício
    mensagem = {
        'nome': fake.name(),
        'endereco': fake.address(),
        'email': fake.email(),
        'timestamp': time.time()
    }
    # Envia mensagem ao Kafka
    producer.send(topic, mensagem)
    print(f"Mensagem enviada: {mensagem}")
    time.sleep(2)  # Intervalo entre mensagens
