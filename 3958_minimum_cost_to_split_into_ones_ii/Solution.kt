// LeetCode 3958 - Minimum Cost To Split Into Ones II
// https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

class Solution {
    fun minCost(n: Int): Long {
        return 1L * n * (n - 1) / 2
    }
}
