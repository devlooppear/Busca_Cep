import requests
CEP = '31275000'

def PegarInfoCep():
    link = f'https://viacep.com.br/ws/{CEP}/json'

    requisicao = requests.get(link)
    return requisicao

def OutPutInfo(requisicao):
    dic_requisicao = requisicao.json()

    print(dic_requisicao)

def main():
    
    requisicao = PegarInfoCep()

    OutPutInfo(requisicao)

main()