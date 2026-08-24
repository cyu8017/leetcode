# LeetCode 3227 - Vowels Game in a String
# https://leetcode.com/problems/vowels-game-in-a-string/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for c in s:
            if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
                return True
        return False
