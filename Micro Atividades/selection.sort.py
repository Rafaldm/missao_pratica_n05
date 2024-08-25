def selectionSort(array):
    # Itera sobre cada elemento do array
    for i in range(len(array)):
        # Inicializa a variável min_idx com o valor de i
        min_idx = i
        
        # Itera sobre o restante do array a partir de i + 1
        for j in range(i + 1, len(array)):
            # Se o elemento atual for menor que o elemento na posição min_idx, atualize min_idx
            if array[j] < array[min_idx]:
                min_idx = j
        
        # Troca os elementos array[i] e array[min_idx]
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]

# Declara um array de números com 15 posições, não ordenados
array_numeros = [64, 34, 25, 12, 22, 11, 90, 78, 45, 23, 56, 89, 1, 7, 39]

# Aplica o método selectionSort no array
selectionSort(array_numeros)

# Imprime o array ordenado
print("Array ordenado com Selection Sort:", array_numeros)
