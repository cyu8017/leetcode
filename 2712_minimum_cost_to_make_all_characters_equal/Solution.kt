// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

class Solution {
    fun minimumCost(s: String): Long {
        val n = s.length
        var ans = 0L
        for (i in 1 until n) {
            if (s[i] != s[i - 1]) ans += minOf(i, n - i).toLong()
        }
        return ans
    }
}
