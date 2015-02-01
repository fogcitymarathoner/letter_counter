__author__ = 'marc'

from lib.letter_counter import LetterCounter

def letter_counts(in_str):
    if len(in_str) == 1:
        lc = LetterCounter(in_str[0])
        return lc.letters
    elif len(in_str) >= 1:
        lc = LetterCounter(in_str[0])
        for l in in_str[1:]:
            if lc.is_counting(l):
                lc.increment(l)
            else:
                lc.append(l)
        return lc.letters
    # null input
    return None