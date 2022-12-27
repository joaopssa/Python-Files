#Criado pelo desenvolvedor João Pedro Silva de Sá

#O Código é dividido em dois passos:

# 1º Passo: Arranjar o número de integrantes X em um número de equipes Y de modo que fiquem bem distribuídos
#           (OBS:Para evitar equipes vazias foi necessário implementar uma condição que impedisse X<Y)
# 2º Passo: Coletar os nomes dos participantes para inserí-los no arranjo feito
#           (OBS:Foi necessário implementar uma nova condição para evitar repetição de nomes e causar ambiguidades)

#Todos os imports utilizados
import random

#Todas as defs utilizadas
def margem():
    print('-'*85)

def erro(x):
    if not x.isnumeric():
        x = input('Favor digitar um número válido: ')
    else:
        return int(x)

def erro_resposta(x):
    respostas = ['SIM','NÃO']
    if x  not in respostas:
        print("Resposta Inválida")
        x = input('Deseja sortear novamente (Sim ou Não) ? ').upper()
    return(x)

#Layout para nortear o usuário
print('SORTEADOR DE EQUIPES')


#Início do loop do sorteador
resposta ='SIM'
while resposta == 'SIM':
    margem()
#Parte da coleta dos números para o 1º Passo
    n_eq = (input('Informe o número de equipes que você deseja formar: '))
    erro(n_eq)
    n_pa = (input('Informe o número de participantes do sorteio: '))
    erro(n_pa)
#Aplicando a def para evitar possíveis erros de entrada do usuário
    n_eq = int(n_eq)
    n_pa = int(n_pa)
    if n_eq>n_pa:
        print('Há equipes demais para pouco participantes! Não há como sortear!')
    
#Parte logística do 1º Passo: Distribuição de participantes por equipe
    else:
        n_pa = int(n_pa)
        n_eq = int(n_eq)
        if n_pa%n_eq==0:
            print('Serão formadas {} equipe(s) com {} participante(s).'.format(n_eq,n_pa//n_eq))
        else:
            print('Serão formadas {} equipe(s) com {} participante(s)  e {} equipe(s) com {} participante(s)'.format(n_pa%n_eq,n_pa//n_eq+1,n_eq -(n_pa%n_eq),n_pa//n_eq))
        margem()
    
#Parte da coleta nome participantes para o 2º Passo
        nomes = []
        for i in range(n_pa):
            part = input('Informe o nome do participante {}: '.format(i+1))
            while part in nomes:
                print("Este nome já foi informado")
                part = input('Informe o nome do participante {}: '.format(i+1))
            nomes.append(part)
        margem()
    
#Parte necessária para misturar os nomes dentro da lista
        random.shuffle(nomes)
    
#Output: Exibindo as equipes
        if n_pa%n_eq==0:
            ref = 0
            for c in range (n_eq):
                print('Equipe formada:')
                print(nomes[ref: ref + len(nomes)//n_eq])
                ref += len(nomes)//n_eq
        
        else:
            ref = 0
            for j in range (n_pa%n_eq):
                print('Equipe formada:')
                print(nomes[ref: ref + len(nomes)//n_eq+1])
                ref += len(nomes)//n_eq+1
            for l in range (n_pa%n_eq+1,1+ n_eq):
                print('Equipe formada:')
                print(nomes[ref: ref + len(nomes)//n_eq])
                ref += len(nomes)//n_eq
#Continuação (ou não) do loop
    margem()
    resposta = input('Deseja sortear novamente (Sim ou Não) ? ').upper()
    resposta = erro_resposta(resposta)
