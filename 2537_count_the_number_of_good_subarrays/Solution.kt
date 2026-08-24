// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

class Solution {
    fun countGood(nums: IntArray, k: Int): Long {
        val freq = HashMap<Int, Int>()
        var pairs = 0L
        var ans = 0L
        var left = 0
        for (right in nums.indices) {
            pairs += freq.getOrDefault(nums[right], 0)
            freq[nums[right]] = freq.getOrDefault(nums[right], 0) + 1
            while (pairs >= k) {
                ans += nums.size - right
                freq[nums[left]] = freq[nums[left]]!! - 1
                pairs -= freq[nums[left]]!!
                left += 1
            }
        }
        return ans
    }
}
