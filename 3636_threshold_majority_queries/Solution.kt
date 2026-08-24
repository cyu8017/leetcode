// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

class Solution {
    fun subarrayMajority(nums: IntArray, queries: Array<IntArray>): IntArray {
        val ans = IntArray(queries.size)
        for (qi in queries.indices) {
            val l = queries[qi][0]
            val r = queries[qi][1]
            val t = queries[qi][2]
            val cnt = HashMap<Int, Int>()
            for (i in l..r) cnt.merge(nums[i], 1) { a, b -> a + b }
            var best = -1
            var bestC = 0
            for ((v, c) in cnt) {
                if (c >= t && (c > bestC || (c == bestC && (best == -1 || v < best)))) {
                    bestC = c
                    best = v
                }
            }
            ans[qi] = best
        }
        return ans
    }
}
