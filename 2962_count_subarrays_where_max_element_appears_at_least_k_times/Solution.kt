// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution {
    fun countSubarrays(nums: IntArray, k: Int): Long {
        var mx = nums[0]
        for (v in nums) { if (v > mx) mx = v }
        var ans = 0
        var cnt = 0
        var left = 0
        for (right in 0 until nums.size) {
            if (nums[right] == mx) cnt++
            while (cnt >= k) {
                if (nums[left] == mx) cnt--
                left++
            }
            ans += left
        }
        return ans
    }
}
