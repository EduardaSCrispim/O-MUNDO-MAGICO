import json
import random
import psutil
from datetime import datetime

from classes.antena import Antena
from classes.firewall import Firewall


def coletar_dados_antena(id_antena):

    rede = psutil.net_io_counters()

    bytes_sent = rede.bytes_sent
    bytes_recv = rede.bytes_recv

    active_conn = random.randint(10, 60)

    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    antena = Antena(
        id_antena,
        bytes_sent,
        bytes_recv,
        active_conn,
        cpu_usage,
        ram_usage,
        timestamp
    )

    return antena


def salvar_antena(antena):

    dados = {
        "ID_antena": antena.id_antena,
        "Bytes_Sent": antena.bytes_sent,
        "Bytes_Recv": antena.bytes_recv,
        "Active_conn": antena.active_conn,
        "CPU_usage": antena.cpu_usage,
        "RAM_usage": antena.ram_usage,
        "timestamp": antena.timestamp
    }

    nome = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    caminho = f"dados/bronze/antenas/{nome}_{antena.id_antena}.json"

    with open(caminho, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


def coletar_dados_firewall():

    rede = psutil.net_io_counters()

    active_sessions = random.randint(50, 200)

    dropped_packets = random.randint(0, 100)

    top_blocked_ip = f"192.168.0.{random.randint(1, 254)}"

    cpu_usage = psutil.cpu_percent(interval=1)

    ram_usage = psutil.virtual_memory().percent

    bytes_sent = rede.bytes_sent
    bytes_recv = rede.bytes_recv

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    firewall = Firewall(
        active_sessions,
        dropped_packets,
        top_blocked_ip,
        cpu_usage,
        ram_usage,
        bytes_sent,
        bytes_recv,
        timestamp
    )

    return firewall


def salvar_firewall(firewall):

    dados = {
        "Active_sessions": firewall.active_sessions,
        "Dropped_packets": firewall.dropped_packets,
        "top_blocked_ip": firewall.top_blocked_ip,
        "CPU_usage": firewall.cpu_usage,
        "RAM_usage": firewall.ram_usage,
        "Bytes_Sent": firewall.bytes_sent,
        "Bytes_Recv": firewall.bytes_recv,
        "timestamp": firewall.timestamp
    }

    nome = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    caminho = f"dados/bronze/firewall/{nome}_firewall.json"

    with open(caminho, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


antenas = ["AP01", "AP02", "AP03", "AP04"]

for antena in antenas:

    dados_antena = coletar_dados_antena(antena)

    salvar_antena(dados_antena)


firewall = coletar_dados_firewall()

salvar_firewall(firewall)


print("Dados das antenas e firewall coletados!")