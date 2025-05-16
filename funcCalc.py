def calculaA(x, y, N):
    somaX = 0
    somaxQuad = 0
    somaY = 0
    multXY = 0

    for i in range(N):
        somaX += x[i]
        somaY += y[i]
        somaxQuad += (x[i] * x[i])
        multXY += (x[i] * y[i])
    
    denominador = N * somaxQuad - (somaX * somaX)
    
    if denominador == 0:
        print("Erro: Divisão por zero.")
        return None
    else:
        a = ((N * multXY) - (somaX * somaY)) / denominador
        return a

def calculaB(x, y, N):
    somaX = 0
    somaxQuad = 0
    multXY = 0
    somaY = 0

    for i in range(N):
        somaX += x[i]
        somaY += y[i]
        somaxQuad += (x[i] * x[i])
        multXY += (x[i] * y[i])

    denominador = N * somaxQuad - (somaX * somaX)
    
    if denominador == 0:
        print("Erro: Divisão por zero.")
        return None
    else:
        b = ((somaxQuad * somaY) - (somaX * multXY)) / denominador
        return b

def main():
    print("Bem-vindo ao calculador de coeficiente de retas!")
    numeroRetas = int(input("Por favor, digite o número de pontos que você gostaria de calcular: "))

    x = [0] * numeroRetas
    y = [0] * numeroRetas

    for i in range(numeroRetas):

        x[i] = float(input(f"Digite o X de número {i+1}: "))
        y[i] = float(input(f"Digite o Y de número {i+1}: "))

    coeficienteA = calculaA(x, y, numeroRetas)
    coeficienteB = calculaB(x, y, numeroRetas)

    if coeficienteA is not None and coeficienteB is not None:
        print(f"Os coeficientes da reta que melhor faz o encaixe são a = {coeficienteA}, b = {coeficienteB}")
    else:
        print("Não foi possível calcular os coeficientes.")

if __name__ == "__main__":
    main()