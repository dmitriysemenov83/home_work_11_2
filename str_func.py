def to_uppercase(line):
    """Функция возвращает результат в виде строки, состоящей из слов в верхнем регистре"""
    return line.upper()


def capitalize_words(string):
    """"Функция возвращает результат в виде строки, состоящей из слов с заглавными первыми буквами"""
    return ' '.join([word.capitalize() for word in string.split()])