// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

class Solution {
    fun countAlternatingSubarrays(nums: IntArray): Long {
        var ans = 1
        var s = 1
        for (i in 1 until nums.size) {
            if (nums[i] != nums[i - 1]) s++
            else s = 1
            ans += s
        }
        return ans
    }
}
