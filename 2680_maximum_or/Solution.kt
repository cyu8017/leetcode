// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

class Solution {
    fun maximumOr(nums: IntArray, k: Int): Long {
        val n = nums.size
        val pref = LongArray(n + 1)
        val suf = LongArray(n + 1)
        for (i in 0 until n) pref[i + 1] = pref[i] or (nums[i].toLong() and 0xffffffffL)
        for (i in n - 1 downTo 0) suf[i] = suf[i + 1] or (nums[i].toLong() and 0xffffffffL)
        var ans = 0L
        for (i in 0 until n) {
            val cur = pref[i] or (nums[i].toLong() shl k) or suf[i + 1]
            if (cur > ans) ans = cur
        }
        return ans
    }
}
