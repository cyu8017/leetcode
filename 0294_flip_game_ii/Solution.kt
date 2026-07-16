// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

class Solution {
    fun canWin(currentState: String): Boolean = canWinMemo(currentState, mutableMapOf())

    private fun canWinMemo(state: String, memo: MutableMap<String, Boolean>): Boolean {
        memo[state]?.let { return it }
        for (index in 0 until state.length - 1) {
            if (state[index] == '+' && state[index + 1] == '+') {
                val nextState = state.substring(0, index) + "--" + state.substring(index + 2)
                if (!canWinMemo(nextState, memo)) {
                    memo[state] = true
                    return true
                }
            }
        }
        memo[state] = false
        return false
    }
}
