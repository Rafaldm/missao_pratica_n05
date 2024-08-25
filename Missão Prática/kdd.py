import time

# Funções de ordenação

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def main():
    # Cria a lista para armazenar as palavras
    palavras = []

    # Lê o arquivo e processa as palavras
    with open('natureza.txt', 'r') as file:
        for linha in file:
            palavras.extend(linha.split())

    # Ordenação e medição de tempo

    # Bubble Sort
    palavras_bubble = palavras.copy()
    start_time = time.time()
    bubble_sort(palavras_bubble)
    bubble_sort_time = time.time() - start_time
    print("Bubble Sort:")
    print(palavras_bubble)
    print(f"Tempo de execução: {bubble_sort_time:.6f} segundos")

    # Selection Sort
    palavras_selection = palavras.copy()
    start_time = time.time()
    selection_sort(palavras_selection)
    selection_sort_time = time.time() - start_time
    print("Selection Sort:")
    print(palavras_selection)
    print(f"Tempo de execução: {selection_sort_time:.6f} segundos")

    # Ordenação nativa
    palavras_sort = palavras.copy()
    start_time = time.time()
    palavras_sort.sort()
    sort_time = time.time() - start_time
    print("Método sort():")
    print(palavras_sort)
    print(f"Tempo de execução: {sort_time:.6f} segundos")

    # Escolha do melhor método
    # No exemplo, vamos escolher o método nativo sort() para salvar o arquivo
    palavras_ordenadas = palavras_sort

    # Salva as palavras ordenadas em um novo arquivo
    with open('palavras_ordenadas.txt', 'w') as file:
        file.write('\n'.join(palavras_ordenadas))

if __name__ == "__main__":
    main()
