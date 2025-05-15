def notaMedia():
    try:
        nota1 = float(input("Digite a 1° nota: ").replace(",", "."))
        nota2 = float(input("Digite a 2° nota: ").replace(",", "."))
        media = (nota1 + nota2) / 2
        
        if media == 10:
            print("Aprovado com Distinção")
        elif media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")
    except ValueError:
        print("valor invalido, tentar novamente")

notaMedia()    
