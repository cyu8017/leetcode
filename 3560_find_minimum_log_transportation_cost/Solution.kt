// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

class Solution {
    fun minCuttingCost(n: Int, m: Int, k: Int): Long {
        var x = maxOf(n, m)
        if (x <= k) return 0
        return 1L * k * (x - k)
    }
}
