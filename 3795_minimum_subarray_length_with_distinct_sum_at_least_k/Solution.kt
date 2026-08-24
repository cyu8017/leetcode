// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum_subarray_length_with_distinct_sum_at_least_k/

class Solution {
    fun minLength(nums: IntArray, k: Int): Int {
        val n = nums.size
        var ans = n + 1
        var l = 0
        val cnt = HashMap<Int, Int>()
        var s = 0L
        for (r in 0 until n) {
            val c = cnt.getOrDefault(nums[r], 0) + 1
            cnt[nums[r]] = c
            if (c == 1) s += nums[r]
            while (s >= k) {
                if (r - l + 1 < ans) ans = r - l + 1
                val left = nums[l]
                val nc = cnt.getOrDefault(left, 0) - 1
                cnt[left] = nc
                if (nc == 0) {
                    cnt.remove(left)
                    s -= left
                }
                l++
            }
        }
        return if (ans > n) -1 else ans
    }
}
