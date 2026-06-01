import random
import time
from datetime import datetime

# ==========================================================
# GLOBAL SOLUTION - SPACE ENERGY MONITOR
# Sistema inteligente de monitoramento energético espacial
# ==========================================================

MODULOS = [
    "Habitação",
    "Comunicação",
    "Suporte à Vida",
    "Painéis Solares",
    "Propulsão",
    "Laboratório"
]


def gerar_dados_simulados():
    """
    Gera dados simulados de uma missão espacial experimental.
    Os valores representam condições operacionais dos módulos.
    """
    dados = []

    for modulo in MODULOS:
        temperatura = round(random.uniform(10, 75), 1)  # graus Celsius
        energia = round(random.uniform(15, 100), 1)     # porcentagem disponível
        potencia = round(random.uniform(0.8, 8.5), 2)   # kW consumidos
        comunicacao = random.choice(["ESTÁVEL", "OSCILANDO", "FALHA"])
        fonte_renovavel = round(random.uniform(20, 100), 1)  # energia solar disponível
        status = "OPERACIONAL"

        dados.append({
            "modulo": modulo,
            "temperatura": temperatura,
            "energia": energia,
            "potencia": potencia,
            "comunicacao": comunicacao,
            "fonte_renovavel": fonte_renovavel,
            "status": status
        })

    return dados


def analisar_modulo(modulo):
    """
    Analisa cada módulo e gera alertas automáticos.
    Também define decisões básicas para situações críticas.
    """
    alertas = []
    decisoes = []
    nivel_risco = 0

    if modulo["temperatura"] >= 60:
        alertas.append("Temperatura crítica detectada")
        decisoes.append("Ativar resfriamento emergencial")
        nivel_risco += 3
    elif modulo["temperatura"] >= 45:
        alertas.append("Temperatura elevada")
        decisoes.append("Aumentar ventilação térmica")
        nivel_risco += 2

    if modulo["energia"] <= 25:
        alertas.append("Energia em nível crítico")
        decisoes.append("Reduzir consumo e priorizar módulos essenciais")
        nivel_risco += 3
    elif modulo["energia"] <= 45:
        alertas.append("Energia baixa")
        decisoes.append("Economizar energia e monitorar consumo")
        nivel_risco += 2

    if modulo["potencia"] >= 7:
        alertas.append("Consumo de potência muito alto")
        decisoes.append("Desligar cargas não essenciais")
        nivel_risco += 2

    if modulo["comunicacao"] == "FALHA":
        alertas.append("Falha de comunicação")
        decisoes.append("Acionar protocolo de comunicação reserva")
        nivel_risco += 3
    elif modulo["comunicacao"] == "OSCILANDO":
        alertas.append("Comunicação instável")
        decisoes.append("Reforçar sinal e verificar antenas")
        nivel_risco += 1

    if modulo["fonte_renovavel"] <= 35:
        alertas.append("Baixa captação de energia solar")
        decisoes.append("Usar baterias auxiliares e ajustar painéis solares")
        nivel_risco += 2

    if nivel_risco >= 6:
        modulo["status"] = "CRÍTICO"
    elif nivel_risco >= 3:
        modulo["status"] = "ATENÇÃO"
    else:
        modulo["status"] = "NORMAL"

    return alertas, decisoes


def classificar_sustentabilidade(dados):
    """
    Calcula uma análise geral de sustentabilidade com base na média
    de energia renovável disponível e no consumo de potência.
    """
    media_renovavel = sum(m["fonte_renovavel"] for m in dados) / len(dados)
    media_potencia = sum(m["potencia"] for m in dados) / len(dados)

    if media_renovavel >= 70 and media_potencia <= 5:
        return "ALTA EFICIÊNCIA SUSTENTÁVEL"
    elif media_renovavel >= 50:
        return "EFICIÊNCIA MODERADA"
    else:
        return "BAIXA EFICIÊNCIA SUSTENTÁVEL"


def exibir_relatorio(dados):
    """
    Exibe os dados monitorados de forma clara e organizada.
    """
    print("\n" + "=" * 72)
    print("        SPACE ENERGY MONITOR - MISSÃO ESPACIAL EXPERIMENTAL")
    print("=" * 72)
    print(f"Data e hora da análise: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 72)

    total_alertas = 0

    for modulo in dados:
        alertas, decisoes = analisar_modulo(modulo)
        total_alertas += len(alertas)

        print(f"\nMÓDULO: {modulo['modulo']}")
        print("-" * 72)
        print(f"Temperatura: {modulo['temperatura']} °C")
        print(f"Energia disponível: {modulo['energia']}%")
        print(f"Potência consumida: {modulo['potencia']} kW")
        print(f"Comunicação: {modulo['comunicacao']}")
        print(f"Energia renovável captada: {modulo['fonte_renovavel']}%")
        print(f"Status do módulo: {modulo['status']}")

        if alertas:
            print("\nALERTAS GERADOS:")
            for alerta in alertas:
                print(f"- {alerta}")
        else:
            print("\nALERTAS GERADOS: Nenhum alerta")

        if decisoes:
            print("\nDECISÕES AUTOMATIZADAS:")
            for decisao in decisoes:
                print(f"- {decisao}")
        else:
            print("\nDECISÕES AUTOMATIZADAS: Manter monitoramento padrão")

    sustentabilidade = classificar_sustentabilidade(dados)

    print("\n" + "=" * 72)
    print("RESUMO GERAL DA MISSÃO")
    print("=" * 72)
    print(f"Total de módulos monitorados: {len(dados)}")
    print(f"Total de alertas gerados: {total_alertas}")
    print(f"Classificação de sustentabilidade: {sustentabilidade}")

    if total_alertas >= 10:
        print("Recomendação geral: aplicar protocolo de segurança máxima.")
    elif total_alertas >= 5:
        print("Recomendação geral: manter equipe em estado de atenção.")
    else:
        print("Recomendação geral: operação estável, manter monitoramento contínuo.")

    print("=" * 72)


def executar_monitoramento(ciclos=3):
    """
    Executa o monitoramento por uma quantidade definida de ciclos.
    """
    for ciclo in range(1, ciclos + 1):
        print(f"\n\nCICLO DE MONITORAMENTO {ciclo}/{ciclos}")
        dados = gerar_dados_simulados()
        exibir_relatorio(dados)

        if ciclo < ciclos:
            time.sleep(2)


if __name__ == "__main__":
    executar_monitoramento()
