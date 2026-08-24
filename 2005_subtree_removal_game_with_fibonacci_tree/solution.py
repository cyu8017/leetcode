# LeetCode 2005 - Subtree Removal Game with Fibonacci Tree
# https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/


class Solution:
    def findGameWinner(self, n: int) -> bool:
        return n % 6 != 1
