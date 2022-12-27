#Criado pelo desenvolvedor João Pedro Silva de Sá

# O Código é dividido em dois passos:
# 1º Passo: Coletar a altura e o peso do participante
#           (OBS:Foi necessário implementar uma função para impedir respostas inválidas para altura ou peso)
# 2º Passo: Calcular e mostrar o IMC relacionando-o com o grau do índice

#Todas as defs utilizadas
def correcao_erros(x):
    if x.isalpha():
        x = input('Favor digitar um valor válido: ')
    else:
        return float(x)
    
def margem():
    print('-'*50)

def erro_resposta(x):
    respostas = ['SIM','NÃO']
    if x  not in respostas:
        print("Resposta Inválida")
        x = input('Deseja calcular novamente (Sim ou Não) ? ').upper()
    return(x)

#Layout para nortear o usuário
print('CALCULADORA DE IMC')

#Início do loop da calculadora
resposta = 'SIM'
while resposta == 'SIM':
    margem()

#Parte da coleta de dados para o 1º Passo
    altura = str(input('Informe sua altura em metros: ').replace(',','.'))
    altura = correcao_erros(altura)
    peso = str(input('Agora informe seu peso em quilogramas: ').replace(',','.'))
    peso = correcao_erros(peso)

#Parte relativa ao cálculo do IMC
    imc = peso / (altura ** 2)
    imc = round(imc, 2)
    imc = str(imc)

# Ao final do cálcuo, utilizo a função replace pois no Brasil a separação decimal é diferente da americana
    imc = imc.replace('.',',')

#Output: Exibindo o IMC e o respectivo resultado com base no IMC
    print('Seu IMC é', imc, end=' ')
# Após registrar o IMC em vírgulas, ele volta a sua versão primária para que assim a calculadora consiga operar
    imc = imc.replace(',','.')
    imc = float(imc)
    if imc < 20:
        print('e é considerado abaixo do normal')
    elif imc < 24.9:
        print('e é considerado normal')
    elif imc < 29.9:
        print('e é considerado obesidade leve')
    elif imc < 39.9:
        print('e é considerado obesidade moderada')
    elif imc > 43:
        print('e é considerado obesidade mórbida')

    margem()
#Continuação (ou não) do loop
    resposta = input('Deseja calcular novamente (Sim ou Não)? ').upper()
    resposta = erro_resposta(resposta)
