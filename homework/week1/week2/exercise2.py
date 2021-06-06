def letter_count(word, letter):
    counter = 0
    for i in word.lower():
        #print(i)
        if i == letter.lower():
            counter = counter + 1
            #print(f'{counter}')
            #print(len(word))
    #print(f'{counter}')
    print(f'Total of letters {letter} used in word {word} is {counter}')

letter_count('Banana', 'a')
letter_count('Banana', 'b')
letter_count('Tarantula', 'T')
letter_count('Tarantula', 'l')