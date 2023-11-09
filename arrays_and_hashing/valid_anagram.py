"""
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.
"""


def valid_anagram(s: str, t: str) -> bool:

    is_an_anagram = True

    s_letter_frequency = {}
    t_letter_frequency = {}

    if (len(s) != len(t)):
        return False

    for i in s:
        if i in s_letter_frequency:
            s_letter_frequency[i] += 1

        else:
            s_letter_frequency[i] = 1

    for j in s:
        if j in t_letter_frequency:
            t_letter_frequency[j] += 1

        else:
            t_letter_frequency[j] = 1

    for key in s_letter_frequency:
        if key in t_letter_frequency:
            if s_letter_frequency[key] != t_letter_frequency[key]:
                is_an_anagram = False
                break
        else:
            is_an_anagram = False
            break

    return is_an_anagram
