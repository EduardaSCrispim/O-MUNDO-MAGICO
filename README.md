 <div align="center">

# O MUNDO MÁGICO

### Projeto de Engenharia de Dados | Data Lake

**Coleta, processamento e análise de dados de infraestrutura de rede.**

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS_S3-FF9900?style=for-the-badge&logo=amazons3&logoColor=white)
![Data Lake](https://img.shields.io/badge/Data_Lake-5541A5?style=for-the-badge)

</div>

---

## Sumário

- [1. Visão geral](#1-visão-geral)
- [2. Arquitetura da solução](#2-arquitetura-da-solução)
- [3. Etapas do processamento](#3-etapas-do-processamento)
- [4. Indicadores e análises](#4-indicadores-e-análises)
- [5. Tecnologias utilizadas](#5-tecnologias-utilizadas)
- [6. Estrutura do projeto](#6-estrutura-do-projeto)
- [7. Aprendizados](#7-aprendizados)

---

## 1. Visão geral

O **O Mundo Mágico** é um projeto de Engenharia de Dados desenvolvido com o objetivo de estruturar um fluxo de coleta, transformação e análise de informações relacionadas à infraestrutura de rede.

A solução trabalha com dados provenientes de antenas e firewall, considerando métricas de desempenho, utilização de recursos computacionais, tráfego de rede e informações relacionadas à segurança.

Para organizar o processamento, o projeto adota a arquitetura **Medallion**, dividindo o fluxo em três camadas: Bronze, Silver e Gold.

Essa organização permite separar os dados brutos, os dados tratados e as informações preparadas para análise, facilitando a manutenção e a evolução do pipeline.

## 2. Arquitetura da solução

A arquitetura é composta por três camadas de processamento:

<details>
<summary><strong>Visualizar fluxo de dados</strong></summary>

```text
       FONTES DE DADOS
        Antenas e Firewall
               |
               v
       +---------------+
       |    BRONZE     |
       | Coleta bruta  |
       |     JSON      |
       +---------------+
               |
               v
       +---------------+
       |    SILVER     |
       | Tratamento e  |
       | consolidação  |
       |      CSV      |
       +---------------+
               |
               v
       +---------------+
       |     GOLD      |
       | Indicadores e |
       |    análises   |
       |      CSV      |
       +---------------+
               |
               v
       DADOS ANALÍTICOS
```

</details>

| Camada | Responsabilidade | Formato |
|---|---|---|
| Bronze | Coleta e armazenamento inicial dos registros | JSON |
| Silver | Tratamento, validação e consolidação | CSV |
| Gold | Organização de dados para análises específicas | CSV |

## 3. Etapas do processamento

### 3.1 Bronze — Coleta de dados

A camada Bronze é responsável pela captura e pelo armazenamento inicial das informações da infraestrutura.

O script `coleta.py` realiza a coleta de métricas relacionadas aos equipamentos monitorados.

Entre as informações consideradas estão:

- Utilização de CPU e memória RAM;
- Tráfego de rede;
- Bytes enviados e recebidos;
- Conexões e sessões ativas;
- Pacotes descartados;
- Endereços IP bloqueados;
- Identificação dos equipamentos e horários de coleta.

Os registros são armazenados em arquivos JSON, preservando os dados em sua forma inicial para as etapas seguintes.

### 3.2 Silver — Tratamento e consolidação

A camada Silver é responsável por transformar os registros coletados em dados organizados e consistentes.

O script `silver.py` realiza operações de processamento, incluindo:

- Leitura dos arquivos de origem;
- Organização dos registros;
- Consolidação das informações;
- Cálculo de throughput de envio e recebimento;
- Classificação de condições de carga;
- Verificação da consistência dos dados de tráfego.

Ao final dessa etapa, os dados tratados são disponibilizados em formato CSV.

### 3.3 Gold — Preparação para análise

A camada Gold organiza os dados consolidados em conjuntos direcionados a análises específicas.

O script `gold.py` gera arquivos CSV destinados à avaliação de diferentes aspectos da infraestrutura.

Essa etapa transforma os dados tratados em informações que facilitam a identificação de comportamentos relevantes e possíveis pontos de atenção.

## 4. Indicadores e análises

O processamento da camada Gold contempla quatro frentes de análise:

| Análise | Objetivo |
|---|---|
| Antenas subutilizadas | Identificar equipamentos com baixa utilização |
| Antenas sobrecarregadas | Identificar equipamentos com alta densidade de conexões |
| Eficiência de hardware | Relacionar indicadores de throughput e utilização de CPU |
| Segurança | Organizar informações sobre sessões, pacotes descartados e IPs bloqueados |

Essas análises permitem explorar o comportamento da infraestrutura sob diferentes perspectivas, apoiando a interpretação dos dados coletados.

## 5. Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| **Python** | Desenvolvimento dos scripts de coleta e processamento |
| **Pandas** | Manipulação, transformação e consolidação de dados |
| **Psutil** | Captura de métricas de sistema e rede |
| **JSON** | Armazenamento dos dados brutos |
| **CSV** | Armazenamento dos dados tratados e analíticos |
| **AWS S3** | Tecnologia considerada no contexto de armazenamento em Data Lake |

## 6. Estrutura do projeto

A organização do repositório separa os scripts de processamento, as classes utilizadas e os diretórios destinados aos dados.

```text
O-MUNDO-MAGICO/
│
├── classes/
│
├── dados/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── coleta.py
├── silver.py
├── gold.py
│
└── README.md
```

### Responsabilidade dos principais scripts

| Arquivo | Responsabilidade |
|---|---|
| `coleta.py` | Captura dos dados de infraestrutura |
| `silver.py` | Tratamento e consolidação dos registros |
| `gold.py` | Geração dos conjuntos de dados analíticos |

## 7. Aprendizados

O desenvolvimento deste projeto possibilitou aplicar conceitos fundamentais de Engenharia de Dados, especialmente:

- Arquitetura Medallion e organização de Data Lakes;
- Coleta de métricas de infraestrutura;
- Manipulação de dados estruturados;
- Processamento e transformação com Python;
- Consolidação de informações em diferentes formatos;
- Construção de indicadores para análise de desempenho e segurança.

---

<div align="center">

**O MUNDO MÁGICO**

Projeto de Engenharia de Dados

Desenvolvido por **Eduarda Santos Crispim**

</div>
