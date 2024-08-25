# Abre o arquivo texto.txt para escrita (se não existir, será criado)
with open('texto.txt', 'w') as file:
    # Cria uma lista e adiciona algumas frases
    texto = list()
    texto.append("Esta é a primeira frase.")
    texto.append("Aqui está a segunda frase.")
    texto.append("Esta é a terceira frase.")
    
    # Escreve cada frase da lista no arquivo
    for linha in texto:
        file.write(linha + '\n')

# Informa que o processo foi concluído
print("Conteúdo da lista foi escrito no arquivo 'texto.txt'.")
