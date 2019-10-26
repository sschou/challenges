from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        return [word[:-1] for word in f]

def calc_word_value(word: str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for c in word:
        if c.isalpha():
            score += LETTER_SCORES[c.upper()]
    return score

def max_word_value(args = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if args is None:
        args = load_words()

    return max(args, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
