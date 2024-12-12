from kafka import KafkaConsumer
import json

# Configuração do Consumer
consumer = KafkaConsumer(
    'meu_topico',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Aguardando mensagens...")

# Consumindo mensagens
for mensagem in consumer:
    print(f"Mensagem recebida: {mensagem.value}")
