import random

# Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir)
# e permitir que o usuário rode o script quantas vezes quiser.

# Detalhes e boas Práticas:
# Você deve desenvolver um projeto em Python que irá rodar inicialmente na linha de comando
# e que, ao ser executado, deverá pergunta o seguinte ao usuário: “Você gostaria de jogar o dado?” Ou alguma variação dessa pergunta.
# Depois de ter feito essa pergunta, o seu programa precisa avaliar a resposta que foi digitado pelo usuário.
# Um passo importante aqui é que, quando digo avaliar quero dizer que você precisa receber o valor, tratar quando ele(a) disser que sim ou que não.
# Seu programa depois deverá fazer a ação necessária de acordo com a resposta que foi entrada pelo usuário.
# Seu script não deve quebrar ou para de funcionar caso o usuário entre algo que não seja esperado, como, por exemplo, um número.
# Trate as exceções ou erros para que seu script rode liso e sem problemas.


print("====== SEJA BEM VINDO!! ======")
print("====== SIMULADOR DE DADOS ======")

#variaveis
jogar = input('Iniciar o Jogo de Dados?: ')
dado = [1, 2, 3, 4, 5, 6]
jogando_dado = "Jogando o Dado.."
x = 0

# jogar
while x != "não":
    if jogar == "não":
        print("Obrigado por Jogar, Volte Sempre.")
        exit()
    elif jogar.isnumeric() or jogar.isspace() or jogar != "sim" and jogar != "não":
        print("Valor digitado é inválido, por gentileza, para conseguir jogar, digite uma opção: (sim) ou (não).")
        exit()
    else:
        print(jogando_dado)
        print(f"O Dado parou no nº: {random.choice(dado)}")
    break


#jogar novamente
while x != "não":
    x = input('Jogar novamente?: ')
    if x.isnumeric() or x.isspace() or x != "sim" and x != "não":
        print("Valor digitado é inválido, por gentileza, para conseguir jogar, digite uma opção: (sim) ou (não).")
        exit()
    elif x == "sim":
        print(jogando_dado)
        print(f"O Dado parou no nº: {random.choice(dado)}")
    else:
        print("Obrigado por Jogar, Volte Sempre.")
        exit()

