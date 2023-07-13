def is_palindrome_recursive(word, low_index, high_index):
    if not word:  # Verificação caso a palavra venha vazia
        return False
    if low_index >= high_index:  # Chegamos ao centro da palavra
        return True
    elif word[low_index] == word[high_index]:  # Chegamos recursivamente a func
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:  # Não é um palíndromo
        return False
