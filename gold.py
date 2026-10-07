import pandas as pd


# Lê os dados do Silver

df = pd.read_csv(
    "dados/silver/dados_consolidados.csv"
)



# 1. ANTENAS SUBUTILIZADAS


antenas_subutilizadas = df[
    df["Active_conn"] < 20
]

antenas_subutilizadas.to_csv(
    "dados/gold/antenas_subutilizadas.csv",
    index=False
)



# 2. ANTENAS SOBRECARREGADAS


antenas_sobrecarregadas = df[
    df["status_carga"] == "Alta densidade"
]

antenas_sobrecarregadas.to_csv(
    "dados/gold/antenas_sobrecarregadas.csv",
    index=False
)



# 3. EFICIÊNCIA DO HARDWARE


df["eficiencia_hardware"] = (
    df["Throughput_Sent_Mbps"]
    / df["CPU_usage"]
)

df["eficiencia_hardware"] = (
    df["eficiencia_hardware"].round(4)
)

df.to_csv(
    "dados/gold/eficiencia_hardware.csv",
    index=False
)



# 4. ANÁLISE DE SEGURANÇA


seguranca = df[
    [
        "ID_antena",
        "Dropped_packets",
        "top_blocked_ip",
        "Active_sessions"
    ]
]

seguranca.to_csv(
    "dados/gold/analise_seguranca.csv",
    index=False
)



# 5. RESUMO


print()
print("========== GOLD ==========")

print()
print("Antenas subutilizadas:")
print(antenas_subutilizadas["ID_antena"].tolist())

print()
print("Antenas sobrecarregadas:")
print(antenas_sobrecarregadas["ID_antena"].tolist())

print()
print("IP mais bloqueado:")
print(df["top_blocked_ip"].iloc[0])

print()
print("Pacotes descartados:")
print(df["Dropped_packets"].iloc[0])

print()
print("Gold gerado com sucesso!")