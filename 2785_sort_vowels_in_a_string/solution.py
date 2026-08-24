# LeetCode 2785 - Sort Vowels in a String
# https://leetcode.com/problems/sort-vowels-in-a-string/


class Solution:
    def sortVowels(self, s: str) -> str:
        def is_vowel(c: str) -> bool:
            return c in "aeiouAEIOU"

        vowels = [c for c in s if is_vowel(c)]
        vowels.sort()
        arr = list(s)
        vi = 0
        for i, c in enumerate(arr):
            if is_vowel(c):
                arr[i] = vowels[vi]
                vi += 1
        return "".join(arr)
