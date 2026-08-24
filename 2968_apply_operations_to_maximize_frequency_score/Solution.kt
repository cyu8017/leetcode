// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

class Solution {
    private fun cost(nums: IntArray, pref: LongArray, l: Int, r: Int): Long {
        var mid = (l + r) / 2
        var left = nums[mid] * (mid - l) - (pref[mid] - pref[l])
        var right = (pref[r + 1] - pref[mid + 1]) - nums[mid] * (r - mid)
        return left + right
    }

    fun maxFrequencyScore(nums: IntArray, k: Long): Int {
        nums.sort()
        var n = nums.size
        var pref = LongArray(n + 1)
        for (i in 0 until n) { pref[i + 1] = pref[i] + nums[i] }
        var ans = 1
        var left = 0
        for (right in 0 until n) {
            while (cost(nums, pref, left, right) > k) left++
            ans = maxOf(ans, right - left + 1)
        }
        return ans
    }
}
