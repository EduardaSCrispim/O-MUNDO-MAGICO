import json
import glob
import pandas as pd



# ANTENAS


arquivos_antenas = glob.glob(
    "dados/bronze/antenas/*.json"
)

antenas = []

for arquivo in arquivos_antenas:

    with open(arquivo, "r") as arquivo_json:

        dados = json.load(arquivo_json)

        antenas.append(dados)



antenas_organizadas = {}

for antena in antenas:

    id_antena = antena["ID_antena"]

    if id_antena not in antenas_organizadas:

        antenas_organizadas[id_antena] = []

    antenas_organizadas[id_antena].append(antena)



# FIREWALL


arquivos_firewall = glob.glob(
    "dados/bronze/firewall/*.json"
)

firewalls = []

for arquivo in arquivos_firewall:

    with open(arquivo, "r") as arquivo_json:

        dados = json.load(arquivo_json)

        firewalls.append(dados)




firewalls.sort(
    key=lambda x: x["timestamp"]
)


# Pega as duas últimas coletas

firewall_anterior = firewalls[-2]

firewall_atual = firewalls[-1]


# Diferença do firewall

firewall_bytes_sent = (
    firewall_atual["Bytes_Sent"]
    - firewall_anterior["Bytes_Sent"]
)

firewall_bytes_recv = (
    firewall_atual["Bytes_Recv"]
    - firewall_anterior["Bytes_Recv"]
)



# SILVER


dados_silver = []

soma_antenas = 0


for id_antena in antenas_organizadas:

    registros = antenas_organizadas[id_antena]

    # Ordena as coletas da antena

    registros.sort(
        key=lambda x: x["timestamp"]
    )


    # Pega as duas últimas

    anterior = registros[-2]

    atual = registros[-1]


    
    # DIFERENÇA DE BYTES
    

    diferenca_bytes_sent = (
        atual["Bytes_Sent"]
        - anterior["Bytes_Sent"]
    )

    diferenca_bytes_recv = (
        atual["Bytes_Recv"]
        - anterior["Bytes_Recv"]
    )


    # Soma o tráfego das antenas

    soma_antenas = (
        soma_antenas
        + diferenca_bytes_sent
    )


 
    # TEMPO
   

    tempo_anterior = pd.to_datetime(
        anterior["timestamp"]
    )

    tempo_atual = pd.to_datetime(
        atual["timestamp"]
    )

    segundos = (
        tempo_atual - tempo_anterior
    ).total_seconds()



    # THROUGHPUT


    if segundos > 0:

        throughput_sent = (
            diferenca_bytes_sent * 8
        ) / segundos / 1000000

        throughput_recv = (
            diferenca_bytes_recv * 8
        ) / segundos / 1000000

    else:

        throughput_sent = 0
        throughput_recv = 0


    
    # STATUS DA CARGA
    

    if atual["Active_conn"] > 40:

        status_carga = "Alta densidade"

    elif atual["CPU_usage"] > 80:

        status_carga = "Gargalo de processamento"

    elif atual["RAM_usage"] > 75:

        status_carga = "Risco de OOM"

    else:

        status_carga = "Normal"


    
    # ADICIONA AO SILVER
  

    dados_silver.append({

        "ID_antena": atual["ID_antena"],

        "Bytes_Sent": atual["Bytes_Sent"],

        "Bytes_Recv": atual["Bytes_Recv"],

        "Active_conn": atual["Active_conn"],

        "CPU_usage": atual["CPU_usage"],

        "RAM_usage": atual["RAM_usage"],

        "Throughput_Sent_Mbps": round(
            throughput_sent, 2
        ),

        "Throughput_Recv_Mbps": round(
            throughput_recv, 2
        ),

        "status_carga": status_carga,

        "timestamp": atual["timestamp"],

        "Active_sessions":
            firewall_atual["Active_sessions"],

        "Dropped_packets":
            firewall_atual["Dropped_packets"],

        "top_blocked_ip":
            firewall_atual["top_blocked_ip"],

        "Firewall_CPU_usage":
            firewall_atual["CPU_usage"],

        "Firewall_RAM_usage":
            firewall_atual["RAM_usage"],

        "Firewall_Bytes_Sent":
            firewall_atual["Bytes_Sent"],

        "Firewall_Bytes_Recv":
            firewall_atual["Bytes_Recv"]

    })



# SALVA CSV


df = pd.DataFrame(dados_silver)

df.to_csv(
    "dados/silver/dados_consolidados.csv",
    index=False
)


# CONSISTÊNCIA DO TRÁFEGO


diferenca_trafego = (
    firewall_bytes_sent
    - soma_antenas
)


print("Dados Silver gerados com sucesso!")

print()
print("----- CONSISTÊNCIA DO TRÁFEGO -----")

print(
    "Bytes enviados pelas antenas:",
    soma_antenas
)

print(
    "Bytes enviados pelo firewall:",
    firewall_bytes_sent
)

print(
    "Diferença:",
    diferenca_trafego
)