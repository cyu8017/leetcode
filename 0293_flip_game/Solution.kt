// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

class Solution {
    fun generatePossibleNextMoves(currentState: String): List<String> {
        val result = mutableListOf<String>()
        for (index in 0 until currentState.length - 1) {
            if (currentState[index] == '+' && currentState[index + 1] == '+') {
                result.add(currentState.substring(0, index) + "--" + currentState.substring(index + 2))
            }
        }
        return result
    }
}
