// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

class Solution {
    fun maximumSubarrayXor(nums: IntArray, queries: Array<IntArray>): IntArray {
        var n = nums.size
        var f = IntArray(n)[]
        for (i in 0 until n) { f[i] = IntArray(n) }
        for (i in 0 until n) { f[i][i] = nums[i] }
        for (length in 2 ..n) {
            var i = 0
            while (i + length - 1 < n) {
                var j = i + length - 1
                f[i][j] = f[i][j - 1] ^ f[i + 1][j]
                i++
            }
        }
        var best = IntArray(n)[]
        for (i in 0 until n) { best[i] = IntArray(n) }
        for (i in 0 until n) { best[i][i] = f[i][i] }
        for (length in 2 ..n) {
            var i = 0
            while (i + length - 1 < n) {
                var j = i + length - 1
                best[i][j] = maxOf(f[i][j], maxOf(best[i][j - 1], best[i + 1][j]))
                i++
            }
        }
        var ans = IntArray(queries.size)
        for (i in 0 until queries.size) { ans[i] = best[queries[i][0]][queries[i][1]] }
        return ans
    }
}
