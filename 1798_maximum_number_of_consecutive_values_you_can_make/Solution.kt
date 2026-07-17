// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

class Solution {
    fun getMaximumConsecutive(coins: IntArray): Int {
        coins.sort()
        var reach = 0L
        for (coin in coins) {
            if (coin > reach + 1) break
            reach += coin
        }
        return (reach + 1).toInt()
    }
}
