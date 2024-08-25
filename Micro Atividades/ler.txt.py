# Abrindo o arquivo e lendo seu conteúdo
with open('loremipsum.txt', 'r') as file:
    conteudo = file.read()

# Imprime o conteúdo completo do arquivo
print("Conteúdo completo do arquivo:")
print(conteudo)

# Imprime a primeira linha do arquivo
with open('loremipsum.txt', 'r') as file:
    primeira_linha = file.readline()
print("\nPrimeira linha do arquivo:")
print(primeira_linha.strip())  # .strip() remove possíveis quebras de linha

# Imprime os 3 primeiros caracteres do arquivo
with open('loremipsum.txt', 'r') as file:
    primeiros_caracteres = file.read(3)
print("\nOs 3 primeiros caracteres do arquivo:")
print(primeiros_caracteres)

# Utilizando a instrução `with` para abrir o arquivo e imprimir o conteúdo
print("\nConteúdo do arquivo usando `with`:")
with open('loremipsum.txt', 'r') as file:
    conteudo_com_with = file.read()
    print(conteudo_com_with)
