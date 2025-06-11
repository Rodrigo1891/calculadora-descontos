def calcular_desconto(preco, desconto_percentual):
    desconto_valor = preco * (desconto_percentual / 100)
    preco_final = preco - desconto_valor
    return preco_final

def main():
    print("=== Calculadora de Descontos ===")
    preco = float(input("Digite o preço do produto: R$ "))
    desconto = float(input("Digite o percentual de desconto (%): "))

    preco_final = calcular_desconto(preco, desconto)
    print(f"Preço final após desconto: R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()
