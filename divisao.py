def divisao(A, B):
    if B == 0:
        return ValueError("Divisão por zero não é permitida.")
    else:
        divisao = A / B
        return divisao