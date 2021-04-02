def count_letters(phrase, count_type='vowels'):
    ''' This function takes a phrase in string format and count it's vowels or consonants.
        Parameter count_type receives "vowels" or "consonants", and the default is "vowels".
    '''

    return sum([phrase.count(i) for i in set(phrase) if i in 'AEIOUaeiou']) if count_type == 'vowels' else sum([phrase.count(i) for i in set(phrase) if i not in ' AEIOUaeiou'])
