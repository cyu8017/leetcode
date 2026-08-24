// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

class Solution {
    private fun canSubsetSum(vals: MutableList<Int>, target: Int): Boolean {
        if (target == 0) return true
        var dp = BooleanArray(target + 1)
        dp[0] = true
        for (v in vals) {
            run {
                var s = target
                while (s >= v) {
                    if (dp[s - v]) dp[s] = true
                    s = s - 1
                }
            }
        }
        return dp[target]
    }

    fun minZeroArray(nums: IntArray, queries: Array<IntArray>): Int {
        var n = nums.size
        if (ok(nums, queries, 0)) return 0
        var lo = 1
        var hi = queries.size + 1
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (mid <= queries.size && ok(nums, queries, mid)) hi = mid
            else lo = mid + 1
        }
        return if (lo > queries.size) -1 else lo
    }

    private fun ok(nums: IntArray, queries: Array<IntArray>, k: Int): Boolean {
        var n = nums.size
        for (i in 0 until n) {
            if (nums[i] == 0) continue
            var vals = ArrayList<Int>()
            for (q in 0 until k) {
                var l = queries[q][0]
                var r = queries[q][1]
                var v = queries[q][2]
                if (l <= i && i <= r) vals.add(v)
            }
            if (!canSubsetSum(vals, nums[i])) return false
        }
        return true
    }
}
