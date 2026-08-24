// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

class Solution {
    fun longestAlternatingSubarray(nums: IntArray, threshold: Int): Int {
        var ans = 0
        var n = nums.size
        for (i in 0 until n) {
            if (nums[i] % 2 != 0 || nums[i] > threshold) continue
            var j = i
            while (j + 1 < n && nums[j + 1] <= threshold && nums[j + 1] % 2 != nums[j] % 2) j++
            ans = maxOf(ans, j - i + 1)
        }
        return ans
    }
}
