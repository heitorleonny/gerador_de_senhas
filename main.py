import random
import string
import time

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    senha = ''
    for i in range(tamanho):
        senha += random.choice(caracteres)
        
    return senha

def gerar_varias_senhas(tamanho, quantidade):
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    lista_senhas = []
    while quantidade > 0:
        senha = ''
        for i in range(tamanho):
            senha += random.choice(caracteres)
        lista_senhas.append(senha,)
        quantidade -= 1
    return lista_senhas



r = True
print('Olá, seja bem vindo ao gerador de senhas!!!')
while r:
    time.sleep(1)
    resposta = int(input('Você deseja gerar quantas senhas?'))
    if int(resposta) < 1:
        print('Por favor, digite um valor válido!')
        continue
    else:
        if resposta == 1:
            time.sleep(1)
            tamanho = int(input('Entendi, agora me diga quantos caracteres você quer que sua senha possua:'))
            senha_gerada = gerar_senha(tamanho)
            print('Aqui está a sua senha:')
            time.sleep(0.5)
            print(senha_gerada)
            time.sleep(1)
            salvar = str(input('Você deseja salvar sua senha em um documento de texto? [s] ou [n]?\n'))
        if resposta > 1:
            time.sleep(1)
            quantidade = resposta
            tamanho = int(input('Entendi, agora me diga quantos caracteres você quer que cada senha possua:'))
            senhas_gerada = gerar_varias_senhas(tamanho, quantidade)
            print('Aqui estão as suas senhas:')
            time.sleep(0.5)
            for senha in senhas_gerada:
                print(senha)
            salvar = input('Você deseja salvar as suas senhas em um documento de texto? [s] ou [n]?\n')
    
    if salvar == 's':
        if resposta == 1:
            with open('senhas.tx', 'w') as arquivo:
                arquivo.write(senha_gerada)
            print('Sua senha foi salva!')
        else:
            with open('senhas.tx', 'w') as arquivo:
                for senha in senhas_gerada:
                    arquivo.write(f'{senha}\n')
            print('Suas senhas foram salvas!')            
        break
        
    
    
    else:
        time.sleep(1)
        print('Ok, até a próxima!')
        break
                
    
            
    
    