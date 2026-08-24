// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

class Solution {
    private fun fee(x: Int): Int {
        if (x == 1) return 1
        if (x > 5) return 3 * x
        return 2 * x
    }

    fun lateFee(daysLate: IntArray): Int {
        var ans = 0
        for (x in daysLate) { ans += fee(x) }
        return ans
    }
}
