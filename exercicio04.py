def qdtParesImpares():
    impar = 0
    par = 0
    try:
        for i in range(10): 
            num = int(float(input(f"Digite o {i+1}° numero: ")))

            if isinstance(num, int) :
            
                if num % 2 == 0:
                    par += 1
                else:
                    impar += 1
            else:
                print("O numero precisa ser inteiro")
        
        print(f"o total de numero pares é {par} ")
        print(f"o total de numero impares é {impar} ")
    except ValueError:
        print("valor inserido invalido, tentar novemente")
qdtParesImpares()