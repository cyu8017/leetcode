// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

class Solution {
    fun minZeroArray(nums: IntArray, queries: Array<IntArray>): Int {
        var n = nums.size
        if (ok(0, nums, queries, n)) return 0
        var lo = 1
        var hi = queries.size + 1
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (mid <= queries.size && ok(mid, nums, queries, n)) hi = mid
            else lo = mid + 1
        }
        if (lo > queries.size) return -1
        return lo
    }

    private fun ok(k: Int, nums: IntArray, queries: Array<IntArray>, n: Int): Boolean {
        var diff = LongArray(n + 1)
        for (i in 0 until k) {
            var q = queries[i]
            diff[q[0]] += q[2]
            diff[q[1] + 1] -= q[2]
        }
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            if (cur < nums[i]) return false
        }
        return true
    }
}
