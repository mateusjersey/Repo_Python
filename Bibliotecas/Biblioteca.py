import os

lista_arquivos = os.listdir('arquivos')
print(lista_arquivos)
# os.rename('arquivos/abr22.txt', 'arquivos/22/abr22.txt')

for arquivos in lista_arquivos:
    if '.txt' in arquivos:
        if '22' in arquivos:
            os.rename(f'arquivos/{arquivos}', f'arquivos/22/{arquivos}')
        else:
            os.rename(f'arquivos/{arquivos}', f'arquivos/23/{arquivos}')

          