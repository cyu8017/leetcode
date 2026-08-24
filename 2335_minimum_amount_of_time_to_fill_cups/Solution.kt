// LeetCode 2335 - Minimum Amount of Time to Fill Cups
// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

class Solution {
    fun fillCups(amount: IntArray): Int {
        amount.sortDescending()
        val a = amount[0]
        val b = amount[1]
        val c = amount[2]
        if (a >= b + c) return a
        return (a + b + c + 1) / 2
    }
}
