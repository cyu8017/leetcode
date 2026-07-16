// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

class Solution {
    private val memo = mutableMapOf<Int, Boolean>()

    fun canIWin(maxChoosableInteger: Int, desiredTotal: Int): Boolean {
        if (desiredTotal <= 0) {
            return true
        }
        val total = maxChoosableInteger * (maxChoosableInteger + 1) / 2
        if (total < desiredTotal) {
            return false
        }
        return canWin(0, 0, maxChoosableInteger, desiredTotal)
    }

    private fun canWin(state: Int, currentTotal: Int, maxChoosableInteger: Int, desiredTotal: Int): Boolean {
        memo[state]?.let { return it }
        for (pick in 1..maxChoosableInteger) {
            val bit = 1 shl (pick - 1)
            if (state and bit != 0) {
                continue
            }
            if (currentTotal + pick >= desiredTotal) {
                memo[state] = true
                return true
            }
            if (!canWin(state or bit, currentTotal + pick, maxChoosableInteger, desiredTotal)) {
                memo[state] = true
                return true
            }
        }
        memo[state] = false
        return false
    }
}
