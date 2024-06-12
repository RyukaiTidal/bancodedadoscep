import mysql.connector
import requests #isso aqui precisa instalar

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="DesafioFinalTurmaA"
)

def acharcep():
    nome1 = input("Insira o nome COMPLETO do Cliente:")
    cursor = banco.cursor()
    CEP = input("Digite seu CEP: ")
    if len(CEP) !=8:
        print('CEP INVALIDO. Terminando o programa.')
        exit()
    print("Verificando endereço")
    endereço = requests.get(f'https://viacep.com.br/ws/{CEP}/json/')
    consulta = endereço.json()
    cep = consulta['cep']
    log = consulta['logradouro']
    comple = consulta['complemento']
    bairro = consulta['bairro']
    localidade = consulta['localidade']
    uf = consulta['uf']
    print(endereço.json())
    cursor = banco.cursor()
    sql = "INSERT INTO Clientes (nome, CEP, Logradouro, Complemento, Bairro, Localidade, uf) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    data = (nome1, cep ,log,comple , bairro,localidade,uf)
    cursor.execute(sql, data)
    banco.commit()
    print("Cliente Inserido")


def mostraraluno():
    meucursor = banco.cursor()
    pesquisa = 'select * from Clientes;'
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for x in resultado:
        print(x)

def sairmenu():
    cursor = banco.cursor()
    cursor.close()
    banco.close()


menu = True

while True:
    print(f'1 - Mostrar Clientes'
          f'\n2 - Inserir Clientes'
          f'\n3 - Sair')
    select = int(input("-"))
    if select == 1:
        mostraraluno()
    elif select == 2:
        acharcep()
    elif select == 3:
        sairmenu()
        print("Obrigado por usar!")
        break
    else:
        print("Comando Incorreto.")

