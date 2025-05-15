def notaMedia():
    nota1 = input("Digite a 1° nota: ")
    nota2 = input("Digite a 2° nota: ")

    media = (nota1 + nota2) / 2
    
    if media == 10:
        print("Aprovado com Distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

notaMedia()    
