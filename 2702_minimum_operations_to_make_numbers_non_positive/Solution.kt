// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

class Solution {
    fun minOperations(nums: IntArray, x: Int, y: Int): Int {
        var lo = 0
        var hi = 0
        for (v in nums) {
            hi = maxOf(hi, (v + y - 1) / y)
            hi = maxOf(hi, (v + x - 1) / x)
        }
        hi += nums.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (ok(nums, x, y, mid)) hi = mid else lo = mid + 1
        }
        return lo
    }

    private fun ok(nums: IntArray, x: Int, y: Int, ops: Int): Boolean {
        var extra = 0L
        for (v in nums) {
            val remain = v - 1L * ops * y
            if (remain > 0) extra += (remain + (x - y) - 1) / (x - y)
        }
        return extra <= ops
    }
}
