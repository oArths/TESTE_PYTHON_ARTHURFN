def ler_inteiro():
    while True:
        entrada = input("Digite um valor inteiro: ")
        try:
            return int(entrada)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def nNumeros():
    nums = []
    op = 1

    while op == 1:
        num = ler_inteiro()
        if num > 0 and num <= 1000:
            nums.append(num)
            op = int(input("Digite 1 para continuar ou qualquer outro dado para parar: "))
        else:
            print("o numero precisa estar entre 0 e 1000")
            
    print(f"\n\n O menor valor é {min(nums)}")
    print(f"\n O maior valor é {max(nums)}")
    print(f"\n A soma dos valor é {sum(nums)}")

nNumeros()