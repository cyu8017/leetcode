// LeetCode 3857 - Minimum Cost To Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

class Solution {
    fun minCost(n: Int): Int {
        return n * (n - 1) / 2
    }
}
