import random

# Criação do array de 15 posições com números aleatórios
array_inteiros = [random.randint(1, 100) for _ in range(15)]
print("Array original (não ordenado):", array_inteiros)

# Ordenação dos dados do array em ordem crescente
array_inteiros.sort()
print("Array ordenado em ordem crescente:", array_inteiros)

# Ordenação dos dados do array em ordem decrescente
array_inteiros.sort(key=None, reverse=True)
print("Array ordenado em ordem decrescente:", array_inteiros)

# Criação de um array de strings
array_strings = ["nome", "dataNascimento", "cpf", "rg"]
print("\nArray original de strings (não ordenado):", array_strings)

# Ordenação dos dados do array de strings em ordem crescente
array_strings.sort()
print("Array de strings ordenado em ordem crescente:", array_strings)

# Ordenação dos dados do array de strings em ordem decrescente
array_strings.sort(key=None, reverse=True)
print("Array de strings ordenado em ordem decrescente:", array_strings)
