# Importando a biblioteca requests
import requests 
import time

# Definindo o URL dos dados oficiais do TSE

# Primeiro turno 
# url = "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"

# Segundo turno 
url = "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"

while True:
    # os.system('cls' if os.name == 'nt' else 'clear')
    # Pegando os dados
    resp = requests.get(url)
    resp = resp.json()

    # Separando os candidatos
    candidatos = resp['cand']
    print(50*'-')
    print(f" ------- TOTAL DE URNAS APURADAS {resp['pst']} -------")
    print(50*'-')
    print("{:20} {:10} {:10}".format("NOME","VOTOS","VOTOS TOTAL"))
    for candidato in candidatos:
        n_1 = 20 - len(candidato['nm'])
        n_2 = 10 
        print("{:20} {:10} {:10}".format(candidato['nm'],candidato['pvap'],candidato['vap']))
    time.sleep(0.5)