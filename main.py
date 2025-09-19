import soma
import subtracao
import multiplicacao
import divisao
import potenciacao

def main():
    print("faça sua operação")
    A = float(input("Digite o primeiro número: "))
    B = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /, **): ")
    if operacao == "+":
        resultado = soma.soma(A, B)
    elif operacao == "-":
        resultado = subtracao.subtracao(A, B)
    elif operacao == "*":
        resultado = multiplicacao.multiplicacao(A, B)
    elif operacao == "/":
        resultado = divisao.divisao(A, B)
    elif operacao == "**":
        resultado = potenciacao.potenciacao(A, B)
    else:
        print("Operação inválida.")
        return 
    print(f"O resultado é: {resultado}")
if __name__ == "__main__":
    main()  