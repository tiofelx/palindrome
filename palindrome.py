## Verificar se a palavra é um palíndromo
def palindromo(palavra):
    # Remove espaços e converte a palavra para minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # Verifica se a palavra é igual à sua reversa
    return palavra == palavra[::-1]

# Solicita ao usuário que insira uma palavra
palavra = input(str("Digite uma palavra para verificar se ela é um palíndromo: "))

# Verifica se a palavra é um palíndromo e exibe o resultado
if palindromo(palavra):
    print(f'{palavra} é um palíndromo!')
else:
    print(f'{palavra} não é um palíndromo.')