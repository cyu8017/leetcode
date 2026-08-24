// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

class Solution {
    fun countSubarrays(nums: IntArray): Int {
        var ans = 0
        var i = 0
        while (i + 2 < nums.size) {
            if (nums[i] * 2 + nums[i + 2] * 2 == nums[i + 1]) ans++
            i++
        }
        return ans
    }
}
