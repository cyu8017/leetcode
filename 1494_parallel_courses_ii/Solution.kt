// LeetCode 1494 - Parallel Courses II
// https://leetcode.com/problems/parallel-courses-ii/

class Solution {
    fun minNumberOfSemesters(n: Int, relations: Array<IntArray>, k: Int): Int {
        val prereq = IntArray(n)
        for (edge in relations) prereq[edge[1] - 1] = prereq[edge[1] - 1] or (1 shl (edge[0] - 1))
        val full = (1 shl n) - 1
        val inf = 1_000_000_000
        val dp = IntArray(1 shl n) { inf }
        dp[0] = 0
        for (mask in 0 until (1 shl n)) {
            if (dp[mask] == inf) continue
            var available = 0
            for (c in 0 until n) {
                if (mask shr c and 1 == 0 && prereq[c] and mask == prereq[c]) {
                    available = available or (1 shl c)
                }
            }
            val choices = mutableListOf<Int>()
            if (Integer.bitCount(available) <= k) {
                choices.add(available)
            } else {
                var sub = available
                while (sub > 0) {
                    if (Integer.bitCount(sub) == k) choices.add(sub)
                    sub = (sub - 1) and available
                }
            }
            for (take in choices) {
                val next = mask or take
                dp[next] = minOf(dp[next], dp[mask] + 1)
            }
        }
        return dp[full]
    }
}
