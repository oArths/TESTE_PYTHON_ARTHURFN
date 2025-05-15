def ler_inteiro( mensagem):
    while True:
        entrada = input(mensagem)
        try:
            return int(entrada)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def nNumeros():
    nums = []
    op = 1

    while op == 1:
        num = ler_inteiro("Digite um valor inteiro:")
        nums.append(num)

        op = ler_inteiro("Digite 1 para continuar ou 0 para parar: ")

    print(f"\n O menor valor é {min(nums)}")
    print(f"O maior valor é {max(nums)}")
    print(f"A soma dos valor é {sum(nums)} \n")

nNumeros()