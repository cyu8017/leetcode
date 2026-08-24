// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

class Solution {
    fun minCapability(nums: IntArray, k: Int): Int {
        var lo = Int.MAX_VALUE
        var hi = Int.MIN_VALUE
        for (x in nums) {
            if (x < lo) lo = x
            if (x > hi) hi = x
        }
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (ok(nums, k, mid)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun ok(nums: IntArray, k: Int, cap: Int): Boolean {
        var cnt = 0
        var i = 0
        while (i < nums.size) {
            if (nums[i] <= cap) {
                cnt += 1
                i += 2
            } else {
                i += 1
            }
        }
        return cnt >= k
    }
}
