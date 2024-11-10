
def find_words_with_combination(text, combination):
    result = []
    words = text.split()

    for word in words:
        if combination in word:
            result.append(word)

    return result

# Пример использования
text = "Этот текст содержит несколько слов. Мы выберем только те слова, которые содержат заданное сочетание букв."
combination = "е"

words_with_combination = find_words_with_combination(text, combination)
print("Слова, содержащие '{}': {}".format(combination, words_with_combination))
