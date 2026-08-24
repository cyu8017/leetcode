// LeetCode 3942 - Minimum Operations To Sort A Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

class Solution {
    fun minOperations(nums: IntArray): Int {
        val n = nums.size
        var zero = 0
        for (i in 0 until n) {
            if (nums[i] == 0) {
                zero = i
                break
            }
        }
        var ans = Int.MAX_VALUE
        if (check(nums, zero, 1)) {
            ans = minOf(ans, zero)
            ans = minOf(ans, n - zero + 2)
        }
        if (check(nums, zero, -1)) {
            ans = minOf(ans, zero + 2)
            ans = minOf(ans, n - zero)
        }
        return if (ans == Int.MAX_VALUE) -1 else ans
    }

    private fun check(nums: IntArray, zero: Int, step: Int): Boolean {
        val n = nums.size
        for (i in 1 until n) {
            val prev = ((zero + (i - 1) * step) % n + n) % n
            val curr = ((zero + i * step) % n + n) % n
            if (nums[prev] > nums[curr]) return false
        }
        return true
    }
}
