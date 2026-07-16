# LeetCode 1119 - Remove Vowels from a String
# https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set("aeiou")
        return "".join(ch for ch in s if ch not in vowels)
