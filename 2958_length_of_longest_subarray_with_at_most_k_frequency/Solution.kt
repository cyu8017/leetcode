// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

class Solution {
    fun maxSubarrayLength(nums: IntArray, k: Int): Int {
        var freq = HashMap<Int, Int>()
        var ans = 0
        var left = 0
        for (right in 0 until nums.size) {
            freq[nums[right]] = freq.getOrDefault(nums[right], 0) + 1
            while (freq[nums[right]] > k) {
                freq[nums[left]] = freq[nums[left]] - 1
                left++
            }
            if (right - left + 1 > ans) ans = right - left + 1
        }
        return ans
    }
}
