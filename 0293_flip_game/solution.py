# LeetCode 0293 - Flip Game
# https://leetcode.com/problems/flip-game/

from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result: list[str] = []
        for index in range(len(currentState) - 1):
            if currentState[index : index + 2] == "++":
                result.append(currentState[:index] + "--" + currentState[index + 2 :])
        return result
