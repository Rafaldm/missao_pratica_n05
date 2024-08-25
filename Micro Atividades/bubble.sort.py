def bubbleSort(array):
    # Itera sobre cada elemento do array
    for i in range(len(array)):
        # Itera sobre o array, diminuindo o número de comparações a cada iteração
        for j in range(0, len(array) - i - 1):
            # Se o elemento atual for maior que o próximo elemento, troca-os
            if array[j] > array[j + 1]:
                # Troca os elementos
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

# Declara um array de números com 15 posições
array_numeros = [64, 34, 25, 12, 22, 11, 90, 78, 45, 23, 56, 89, 1, 7, 39]

# Aplica o método bubbleSort no array
bubbleSort(array_numeros)

# Imprime o array ordenado
print("Array ordenado com Bubble Sort:", array_numeros)
