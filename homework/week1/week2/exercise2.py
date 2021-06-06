def letter_count(word, letter):
    counter = 0
    total_sum =0
    while counter <= len(word):
        if letter == word.count(letter):
            total_sum = total_sum + letter
        counter = letter + 1
        print(f'Total of letters {letter} used in word {word} is {total_sum}')

letter_count('Banana', 'a')
