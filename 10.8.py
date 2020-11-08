def samoedlinnoe():
    a = str('Самое замечательное в жизни — возможность записывать свои мысли и чувства')
    maximum = 0
    for index, word in enumerate(a.split()):
        if len(word) > maximum:
            i = index
            maximum = len(word)
    print(f'Слово длиной {maximum} находится на позиции {i + 1}')
samoedlinnoe()