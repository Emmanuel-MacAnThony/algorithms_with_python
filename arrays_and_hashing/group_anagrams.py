from typing import List

"""
    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
"""


def group_anagrams(strs: List[str]):

    anagramMap = {}

    for word in strs:
        anagramKey = ''.join(sorted(word))
        anagramMap[anagramKey] = [word] + anagramMap.get(anagramKey, {})

    anagramGroupings = []

    for key in anagramMap:
        anagramGroupings.append(anagramMap[anagramKey])

    return anagramGroupings
