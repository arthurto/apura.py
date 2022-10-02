# Importando a biblioteca requests
import requests 
import os 
import time

# Definindo o URL dos dados oficiais do TSE
url = "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    # Pegando os dados
    resp = requests.get(url)
    resp = resp.json()

    # Separando os candidatos
    candidatos = resp['cand']
    print(f"NOME {20*'-'} VOTOS % {10*'-'} VOTOS TOTAL")
    for candidato in candidatos:
        n_1 = 20 - len(candidato['nm'])
        n_2 = 10 
        print(f"{candidato['nm']}  {n_1*'-'}  {candidato['pvap']}  {n_2*'-'}  {candidato['vap']} ")
    time.sleep(1)

