def nNumeros():
    nums = []
    op = 1

    while op == 1:
        num = int(float(input("Digite um numero inteiro: ").replace(",",".")))
        nums.append(num)

        op = int(input("Digite 1 para continuar ou qualquer outro dado para parar: "))

    print(f"\n\n O menor valor é {min(nums)}")
    print(f"\n O maior valor é {max(nums)}")
    print(f"\n A soma dos valor é {sum(nums)}")

nNumeros()