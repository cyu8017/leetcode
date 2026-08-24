// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

class Solution {
    fun minCosts(cost: IntArray): IntArray {
        var n = cost.size
        var ans = IntArray(n)
        var mi = cost[0]
        for (i in 0 until n) {
            mi = minOf(mi, cost[i])
            ans[i] = mi
        }
        return ans
    }
}
