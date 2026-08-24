// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution {
    fun minimumSumSubarray(nums: List<Int>, l: Int, r: Int): Int {
        val n = nums.size
        val pref = IntArray(n + 1)
        for (i in 0 until n) pref[i + 1] = pref[i] + nums[i]
        var ans = Int.MAX_VALUE
        var found = false
        for (i in 0 until n) {
            var length = l
            while (length <= r && i + length <= n) {
                val s = pref[i + length] - pref[i]
                if (s > 0 && s < ans) {
                    ans = s
                    found = true
                }
                length++
            }
        }
        return if (found) ans else -1
    }
}
