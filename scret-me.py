#Project by @wandson.dev

#Importqndo
import requests
import json
import os
import time
import sys

#Cores
f = '\033[m'
vermelho = '\033[31m'
v = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'

#Formatando Link
def extract_user_id(link):
    match = re.search(r'https?://scret.me/(\w+)', link)
    if match:
        return match.group(1)
    else:
        return None

#Função Principal
def scret():
    os.system('clear')
    print(f'{amarelo}Projeto by {f}{ciano}@wandson.dev 🤠\n{f}')
    time.sleep(2)
    
    if len(sys.argv) > 1:
        link = sys.argv[1]
    else:
        link = input(f'{azul}Digite o Link do scret.me do Usuário: {f}')
    
    # Verifica e adiciona o prefixo se necessário
    if not link.startswith(('http://', 'https://')):
        link = f'https://{link}'
    
    user_id = extract_user_id(link)
    if user_id is None:
        print(f'{vermelho}[!] Link inválido. Certifique-se de usar um link do scret.me.{f}')
        return

    mensagem = input(f'{azul}Mensagem que será enviada: {f}')
    Contagem = int(input(f'{azul}Quantas Vezes?: {f}'))
    print(f'{azul}**********************************************************{f}')

    valor = 0
    nao_enviado = 0

    while valor < Contagem:

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/json"
        }

        data = {
            "slug": user_id,
            "content": mensagem,
            "device": json.dumps({
                "country_code": "Not found",
                "country_name": "Not found",
                "city": "Not found",
                "postal": "Not found",
                "latitude": "Not found",
                "longitude": "Not found",
                "IPv4": "Not found",
                "state": "Not found",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            }),
            "tips": []
        }

        response = requests.post(
            url="https://api.scret.me/v1/message",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            nao_enviado = 0
            valor += 1
            print(f'{v}[+]{f}Enviado =>{v}{valor}{f}')
        else:
            nao_enviado += 1
            print(f'{vermelho}[-]{f}Não Enviado')

        if nao_enviado == 10:
            print(f'{vermelho}[!]{f}Aguarde 5 Segundos')
            time.sleep(5)
            nao_enviado = 0

    print(f'{amarelo}Projeto by {f}{ciano}@wandson.dev 🤠{f}')

scret()