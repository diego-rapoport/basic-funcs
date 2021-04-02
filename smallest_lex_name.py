def smallest_lex_name(names):
    ''' This function takes a list of names and returns the smallest name lexicographically,
        which means almost like a common dictionary order but capital letters always comes first.

        Ex.:
            With names ['anne', 'jane', 'Brody', 'Carol'] the name "Brody" returns instead of "anne"
            because it's capitalized.

        It can extend to words in general, but the exercise was about names.
    '''

    return names[min([[len(name.strip()), index] for index, name in enumerate(names)])[-1]].strip().capitalize()
