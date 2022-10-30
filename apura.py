# Importando bibliotecas úteis
import requests 
import time

# Definindo o URL dos dados oficiais do TSE

# Primeiro turno 
# url = "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"

# Segundo turno 
url = "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"

while True:

    # Otendo os dados através de um GET request
    resp = requests.get(url)

    # Convertendo as informações em JSON -> dict 
    resp = resp.json()

    # Selecionando as informações dos candidatos
    candidatos = resp['cand']

    # Deixando tudo bonitinho
    print(f"\n ------- TOTAL DE URNAS APURADAS {resp['pst']} ------- \n")

    # Organizando a formatação da tabela (Obrigado Rafa!)
    print("{:20} {:10} {:10}".format("NOME","VOTOS","VOTOS TOTAL"))

    # Loop nos candidatos 
    for candidato in candidatos:

        # Printando informações de cada candidato
        print("{:20} {:10} {:10}".format(candidato['nm'],candidato['pvap'],candidato['vap']))

    # Atualizando a cada meio segundo para não sobrecarregar a API
    time.sleep(0.5)