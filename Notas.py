nota = float(input('Digite sua nota:'))

if 0 <= nota <= 3:
    print(f'Sua nota foi {nota:.1f}. Situação: Reprovado!')

elif 4 <= nota <= 6:
    print(f'Sua nota foi {nota:.1f}. Situação: Recuperação')

elif 7 <= nota <= 10:
    print(f'Sua nota foi {nota:.1f}. Situação: Aprovado')

else:
    print('Por gentileza, coloque um valor valido') #Imginar que o professor entregou a prova dos alunos e as notas estão nas folhas!