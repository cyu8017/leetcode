// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

class Solution {
    fun validSubarrays(nums: IntArray, k: Int): Long {
        var n = nums.size
        var peaks = ArrayList<Int>()
        for (i in 1 until n - 1) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) peaks.add(i)
        }
        var ans = 0
        for (j in 0 until peaks.size) {
            var p = peaks[j]
            var leftMin = maxOf(p - k, 0)
            if (j > 0) leftMin = maxOf(leftMin, peaks[j - 1] + 1)
            var rightMax = minOf(p + k, n - 1)
            if (j < peaks.size - 1) rightMax = minOf(rightMax, peaks[j + 1] - 1)
            ans += (p - leftMin + 1) * (rightMax - p + 1)
        }
        return ans
    }
}
