// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

class Solution {
    fun minDifference(nums: IntArray, queries: Array<IntArray>): IntArray {
        val n = nums.size
        val pref = Array(n + 1) { IntArray(101) }
        for (i in nums.indices) {
            pref[i + 1] = pref[i].clone()
            pref[i + 1][nums[i]]++
        }
        return IntArray(queries.size) { qi ->
            val left = queries[qi][0]
            val right = queries[qi][1]
            var prev = -1
            var best = Int.MAX_VALUE
            for (value in 1..100) {
                if (pref[right + 1][value] - pref[left][value] > 0) {
                    if (prev != -1) best = minOf(best, value - prev)
                    prev = value
                }
            }
            if (best == Int.MAX_VALUE) -1 else best
        }
    }
}
