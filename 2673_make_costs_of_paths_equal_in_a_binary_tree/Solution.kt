// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution {
    fun minIncrements(n: Int, cost: IntArray): Int {
        var ans = 0
        for (i in n / 2 - 1 downTo 0) {
            val l = 2 * i + 1
            val r = 2 * i + 2
            ans += kotlin.math.abs(cost[l] - cost[r])
            cost[i] += maxOf(cost[l], cost[r])
        }
        return ans
    }
}
