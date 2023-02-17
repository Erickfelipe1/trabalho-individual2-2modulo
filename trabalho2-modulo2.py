
candidatos = {}
candidatos_aprovados_vaga1 = {}
candidatos_aprovados_vaga2 = {}

def cadastrar_candidato():
    nome = input("Digite o nome do candidato: ")
    vaga = input("Digite o número da vaga para a qual deseja se candidatar (1 ou 2): ")
    experiencia = input("Digite um breve Resumo sobre suas habilidades e experiências: ")
    candidatos[nome] = {"vaga": vaga, "experiencia": experiencia}

def avaliar_candidatos():
    for nome, info in candidatos.items():
        if info["vaga"] == "1" and "Python" in info["experiencia"] and "programação" in info["experiencia"]:
            candidatos_aprovados_vaga1[nome] = info["experiencia"]
        elif info["vaga"] == "2" and "Análise de dados" in info["experiencia"] and "SQL" in info["experiencia"]:
            candidatos_aprovados_vaga2[nome] = info["experiencia"]


def exibir_resultados():
    print(f"Total de candidatos: {len(candidatos)}")
    print(f"Total de candidatos aprovados para a vaga 1: {len(candidatos_aprovados_vaga1)}")
    print(f"Total de candidatos aprovados para a vaga 2: {len(candidatos_aprovados_vaga2)}")
    print("Candidatos aprovados para a vaga 1:")
    for nome, experiencia in candidatos_aprovados_vaga1.items():
        print(f"{nome}: {experiencia}")
    print("Candidatos aprovados para a vaga 2:")
    for nome, experiencia in candidatos_aprovados_vaga2.items():
        print(f"{nome}: {experiencia}")

while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar candidato")
    print("2 - Avaliar candidatos aprovados")
    print("3 - Exibir resultados")
    print("0 - Sair")
    opcao = input()
    
    if opcao == "1":
        cadastrar_candidato()
    elif opcao == "2":
        avaliar_candidatos()
    elif opcao == "3":
        exibir_resultados()
    elif opcao == "0":
        break
    else:
        print("Opção inválida, tente novamente.")


