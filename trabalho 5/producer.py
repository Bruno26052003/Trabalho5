from kafka import KafkaProducer
from faker import Faker
import json
import time

# Configuração do Producer
producer = KafkaProducer(
    bootstrap_servers=['kafka1:9092', 'kafka2:9093', 'kafka3:9094'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Nome do tópico
topic = 'meu_topico'

# Dados de exemplo
dados_exemplo = [
    {'nome': 'João Silva', 'endereco': 'Rua A, 123', 'email': 'joao@example.com'},
    {'nome': 'Maria Oliveira', 'endereco': 'Avenida B, 456', 'email': 'maria@example.com'},
    {'nome': 'Carlos Pereira', 'endereco': 'Praça C, 789', 'email': 'carlos@example.com'}
]

# Envia as mensagens
for dado in dados_exemplo:
    mensagem = {**dado, 'timestamp': time.time()}
    producer.send(topic, mensagem)
    print(f"Mensagem enviada: {mensagem}")
    time.sleep(2)

