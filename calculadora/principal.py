
import multiplicação
import subtracao
import soma
import divisao
print("bem vindo a calculadora")
print("1:soma 2: divisão 3:multiplicação 4:subtração")
escolha = input("Digite o que deseja fazer")
valor1 = int(input("primeiro valor"))
valor2 = int(input("segundo valor"))

if escolha == "+":
    a = soma.soma(valor1, valor2)

elif escolha == "/":
    a = divisao.dividir(valor1, valor2)

elif escolha == "*":
    a = multiplicação.multiplicacao(valor1, valor2)

elif escolha == "-":
    a = subtracao.subtracao(valor1, valor2)
else:
    print('Operação falhou!')
    
print(f'O calculo {valor1} {escolha} {valor2} = {a}')